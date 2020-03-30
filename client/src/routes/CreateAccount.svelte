<script>
  import { goto } from "@sapper/app";

  let name = "";
  let emailAddress = "";
  let password = "";
  let confirmpassword = "";

  function handleCreate() {
    if (password === confirmpassword) {
      fetch("https://folda-box-office-system.herokuapp.com/users/", {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name,
          emailAddress,
          password
        })
      }).then(r => {
        if (r.ok) {
          goto("/SignIn");
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
  .emails,
  .passwordsetting,
  .confirmpassword,
  .createandsignin {
    padding: 1rem;
  }

  .signin {
    background: transparent;
    color: #4045ed;
    font-style: italic;
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
  <div class="emails">
    <h3>Email</h3>
    <input bind:value={emailAddress} />
  </div>
  <div class="passwordsetting">
    <h3>Password</h3>
    <input type="password" bind:value={password} />
  </div>
  <div class="confirmpassword">
    <h3>Confirm Password</h3>
    <input type="password" bind:value={confirmpassword} />
  </div>
  <div class="createandsignin">
    <button class="create" on:click={handleCreate}>
      <h3>Create Account</h3>
    </button>
    <button class="signin" onclick="location='Signin'">
      <h3>Sign in</h3>
    </button>
  </div>
</div>
