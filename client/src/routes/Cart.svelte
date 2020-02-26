
<script>

  import Panel from "../components/Panel.svelte";

  let cart = [
    {
      name: "Event name",
      artist: "John Smith",
      quantity: 2,
      pricePerTicket: 12.5,
      date: "2020-04-04"
    },
    {
      name: "Fun weekend pass",
      artist: "Multiple",
      quantity: 4,
      pricePerTicket: 6,
      date: "2020-02-02"
    }
  ]; // TODO: fetch this from the server
</script>

<style>
  .headingWrapper {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
  .headingWrapper > * {
    margin: 0;
  }

  .headingWrapper > button {
    margin-left: 1rem;
  }

  .twoColumns {
    display: flex;
  }

  .cartItem {
    display: flex;
    margin: 1rem 0;
    align-items: center;
  }

  .cartItem .imgPlaceholder {
    height: 5rem;
    width: 5rem;
    border-radius: 50%;
    border: 2px solid #555;
    background-color: var(--offwhite);
    margin-right: 1rem;
  }

  .cartItemHeading {
    display: flex;
    font-size: 1.4rem;
    align-items: center;
  }
  .cartItemHeading h4 {
    margin: 0;
    padding: 0;
    font-weight: bold;
    text-decoration: underline;
  }

  .cartItemHeading time {
    margin: 0;
    padding: 0;
    margin-left: 1rem;
  }

  .artistName {
    font-style: italic;
  }
  .removeButtonWrapper {
    margin-left: 1.5rem;
    display: flex;
    justify-content: flex-end;
    flex-grow: 1;
  }
</style>

<svelte:head>
  <title>Cart</title>
</svelte:head>
<div class="headingWrapper">
  <h1>Checkout</h1>
  <button>Add More</button>
</div>

<div class="twoColumns">
  <Panel title="Cart">
    {#each cart as item}
      <div class="cartItem">
        <div class="imgPlaceholder" />
        <div>
          <div class="cartItemHeading">
            <h4>{item.name}</h4>
            <time datetime={item.date}>{item.date}</time>
          </div>
          <div class="artistName">{item.artist}</div>
          <div class="priceAndQuantity">
            {item.quantity} &times; ${item.pricePerTicket}
          </div>
        </div>
        <div class="removeButtonWrapper">
          <button>Remove</button>
        </div>
      </div>
    {/each}
  </Panel>
  <Panel title="Total">
    Tickets: ${cart.map(x => x.pricePerTicket * x.quantity).reduce((a, b) => a + b, 0)}
    <br />
    Tax: $$$
    <br />
    Total: $$$
  </Panel>
</div>
