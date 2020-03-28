<script>
  import { goto } from "@sapper/app";
  import { onMount } from "svelte";

  import Panel from "../components/Panel.svelte";
  import IndividualCartItem from "../components/IndividualCartItem.svelte";
  import DayPassCartItem from "../components/DayPassCartItem.svelte";
  import { userId, jwt } from "../stores.js";

  let purchased = [];
  let subtotal = 0;
  let tax = 0;
  let total = 0;

  const refreshCart = async () => {
    const res = await fetch(
      `http://localhost:5000/users/${$userId}/purchased/`,
      {
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${$jwt}`
        }
      }
    );
    if (res.ok) {
      const data = await res.json();
      purchased = data.purchasables.map(purchasable => ({
        ...purchasable,
        artists: purchasable.events.map(event => event.artistName).join(", "),
        ticketPriceSum: purchasable.tickets.reduce(
          (a, b) => a + b.ticketClass.price,
          0
        )
      }));
      subtotal = data.ticketSubTotal;
      tax = data.tax;
      total = data.totalPrice;
    } else {
      alert("Something went wrong. Please try again in a moment.");
    }
  };

  onMount(refreshCart);

  setTimeout(refreshCart, 3000);

  const groupTicketsByClass = tickets => {
    const dict = {};
    tickets.forEach(t => {
      if (dict.hasOwnProperty(t.ticketClass_id)) {
        dict[t.ticketClass_id].quantity += 1;
      } else {
        dict[t.ticketClass_id] = {
          quantity: 1,
          price: t.ticketClass.price,
          ticketClass: t.ticketClass.description
        };
      }
    });
    return Object.keys(dict).map(key => dict[key]);
  };

  const round = num => Math.ceil(num * 100) / 100;

  const buyTickets = () => {
    goto("/ConfirmPurchase");
  };
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
</style>

<svelte:head>
  <title>Cart</title>
</svelte:head>
<div class="headingWrapper">
  <h1>Purchased Tickets</h1>
</div>
<!-- <code>{JSON.stringify(purchased)}</code> -->
<Panel title="Cart">
  {#each purchased as purchasable}
    {#if purchasable.type == 'individual'}
      <IndividualCartItem
        purchased
        {refreshCart}
        {groupTicketsByClass}
        {purchasable} />
    {:else}
      <DayPassCartItem
        purchased
        {refreshCart}
        {groupTicketsByClass}
        {purchasable} />
    {/if}
  {/each}
  {#if !purchased.length}
    No tickets yet!
    <a href="/">Browse events here</a>
    .
  {/if}
</Panel>
