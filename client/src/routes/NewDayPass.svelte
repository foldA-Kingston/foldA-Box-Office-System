<script>
  import { goto } from "@sapper/app";

  let name = "";

  function handleCreate() {
    if (password === confirmpassword) {
      fetch("http://localhost:5000/events/", {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name
        })
      }).then(r => {
        if (r.ok) {
          const id = 1;
          goto(`/individual-events/${id}`);
        } else {
          alert("Something went wrong. Please try again in a moment.");
        }
      });
    } else {
      alert("Passwords do not match");
    }
  }
</script>

<style>
  .panel {
    width: 40%;
    border-radius: 4px;
    border: 1px solid #333;
    overflow: hidden;
    margin: 1rem 0.5rem;
    padding: 0.5rem;
  }
  .name,
  .confirm {
    padding: 1rem;
  }
</style>

<svelte:head>
  <title>Account</title>
</svelte:head>

<div>
  <h1>Account</h1>
</div>
<div class="panel">
  <div class="name">
    <h3>Name</h3>
    <input bind:value={name} />
  </div>

  <div class="confirm">
    <button class="create" on:click={handleCreate}>
      <h3>Create Account</h3>
    </button>
  </div>
</div>
