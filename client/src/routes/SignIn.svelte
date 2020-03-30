<script>
  import { jwt, emailAddress, isAdmin, userId } from "../stores.js";
  import { goto } from "@sapper/app";

  let email = "";
  let password = "";

  const signIn = async () => {
    const result = await fetch(
      "https://folda-box-office-system.herokuapp.com/auth/",
      {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          emailAddress: email,
          password
        })
      }
    );
    const data = await result.json();

    jwt.set(data.access_token);
    emailAddress.set(data.emailAddress);
    isAdmin.set(data.isAdmin ? "yes" : "no");
    userId.set(data.userId);

    goto("/");
    // TODO: set more info here, like user's name and email
  };
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
  .emails {
    padding: 1rem;
  }
  .password {
    padding: 1rem;
  }
  .createaccount {
    background: transparent;
    color: #4045ed;
    font-style: italic;
  }
  .signinandcreate {
    padding: 1rem;
  }
  .signin {
    margin-right: 2rem;
  }
</style>

<svelte:head>
  <title>Signin</title>
</svelte:head>

<div>
  <h1>Sign In</h1>
</div>
<div class="panel">
  <div class="emails">
    <h3>Email</h3>
    <input bind:value={email} />
  </div>
  <div class="password">
    <h3>Password</h3>
    <input type="password" bind:value={password} />
  </div>

  <div class="signinandcreate">
    <button class="signin" on:click={signIn}>Sign in</button>
    <a class="createaccount" href="/CreateAccount">
      <h3>Create Account</h3>
    </a>
  </div>
</div>
