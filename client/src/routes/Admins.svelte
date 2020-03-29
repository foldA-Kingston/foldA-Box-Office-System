<script>
  import { onMount } from "svelte";
  import { jwt, userId } from "../stores";
  import Panel from "../components/Panel.svelte";

  let admins = [];

  const getAdmins = async () => {
    admins = await fetch("http://localhost:5000/admins/", {
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      }
    }).then(r => r.json());
  };

  onMount(() => {
    getAdmins();
  });

  let newAdminEmail = "";

  $: addAdmin = async () => {
    await fetch("http://localhost:5000/admins/", {
      mode: "cors",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      },
      body: JSON.stringify({ emailAddress: newAdminEmail })
    });
    getAdmins();
  };

  const removeAdmin = async id => {
    await fetch(`http://localhost:5000/admins/${id}/`, {
      mode: "cors",
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      }
    });
    getAdmins();
  };
</script>

<style>
  table {
    width: 100%;
  }
</style>

<Panel title="Administrators">
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th />
      </tr>
    </thead>
    <tbody>
      {#each admins as admin}
        <tr>
          <td>{admin.name}</td>
          <td>{admin.emailAddress}</td>
          <td>
            {#if Number(admin.id) !== Number($userId)}
              <button on:click={() => removeAdmin(admin.id)}>
                Demote from admin
              </button>
            {:else}
              <em>(You)</em>
            {/if}
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</Panel>
<Panel title="Add administrator">
  <label for="email">Email address:</label>
  <br />
  <input id="email" name="email" type="email" bind:value={newAdminEmail} />
  <button on:click={addAdmin}>Add</button>
</Panel>
