<script>
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
        alt="Italian Trulli" />
    </li>
    <li>
      <a class:selected={segment === 'index'} href="">Events</a>
    </li>
    <li>
      <a class:selected={segment === 'DayPasses'} href="DayPasses">DayPasses</a>
    </li>
    <li>
      <a class:selected={segment === 'Cart'} href="Cart">Cart</a>
    </li>
    <li>
      <a class:selected={segment === 'Account'} href="Account">Account</a>
    </li>
  </ul>
</nav>
