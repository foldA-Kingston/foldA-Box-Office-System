<script>
  import { jwt, userId, isAdmin, emailAddress } from "../stores.js";
  export let segment;
</script>

<style>
  nav {
    border-bottom: 2px solid rgba(0, 0, 0, 0.486); /*blue: 64, 69, 237 orange :249, 164, 80*/
    color: var(--blue);
    font: "Poppins";
    font-weight: 400;
    padding: 0 1em;
  }

  ul {
    margin: 1;
    padding: 0;
    display: flex;
    align-items: center;
  }

  /* clearfix */
  ul::after {
    content: "";
    display: block;
    clear: both;
  }

  li {
    display: block;
    float: left;
  }

  .selected {
    position: relative;
    display: inline-block;
  }

  .selected::after {
    position: absolute;
    content: "";
    width: calc(100% - 1em);
    height: 2px;
    background-color: var(--orange);
    display: block;
    bottom: -1px;
  }

  a {
    text-decoration: none;
    padding: 1em 0.5em;
    display: block;
  }
</style>

<nav>
  <ul>
    <li>
      <img
        src="https://www.folda.ca/wp-content/themes/folda/assets/img/logo_footer.svg"
        alt="foldA Logo" />
    </li>
    <li>
      <a class:selected={segment === ''} href="/">Events</a>
    </li>
    <li>
      <a class:selected={segment === 'Accessibility'} href="Accessibility">
        Accessibility
      </a>
    </li>
    {#if $jwt}
      <li>
        <a class:selected={segment === 'Cart'} href="Cart">Cart</a>
      </li>
      <li>
        <a class:selected={segment === 'MyTickets'} href="MyTickets">
          My Tickets
        </a>
      </li>
      <li>
        <a class:selected={segment === 'Account'} href="Account">Account</a>
      </li>
    {/if}
    <li>
      <a class:selected={segment === 'Questionnaire'} href="Questionnaire">
        Questionnaire (?)
      </a>
    </li>
    <li>
      {#if $jwt}
        <button
          on:click={() => {
            jwt.set('');
            userId.set('');
            isAdmin.set('');
            emailAddress.set('');
          }}>
          Log out
        </button>
      {:else}
        <a class:selected={segment === 'SignIn'} href="SignIn">Log in</a>
      {/if}
    </li>
  </ul>
</nav>
