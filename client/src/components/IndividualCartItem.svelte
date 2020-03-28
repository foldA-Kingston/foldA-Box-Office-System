<script>
  export let purchased;
  export let purchasable;
  export let groupTicketsByClass;
  export let refreshCart;
  import { userId, jwt } from "../stores.js";
  import { formatDate } from "../utils.js";

  const removeFromCart = () => {
    fetch(`http://localhost:5000/users/${$userId}/cart/${purchasable.id}/`, {
      mode: "cors",
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      }
    }).then(r => {
      if (r.ok) {
        refreshCart();
      } else {
        alert("Something went wrong. Please try again in a moment.");
      }
    });
  };

  const event = purchasable.events[0];
</script>

<style>
  .cartItem {
    display: flex;
    margin: 1rem 0;
    align-items: flex-start;
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

<div class="cartItem">
  <div class="imgPlaceholder" />
  <div>
    <div class="cartItemHeading">
      <h4>
        Individual event:
        <a href={`/individual-events/${purchasable.events[0].id}`}>
          {purchasable.name}
        </a>
      </h4>
    </div>
    <!-- {JSON.stringify(purchasable)} -->
    <div class="artistName">{purchasable.artists}</div>
    <div class="startEnd">
      <strong>Start:</strong>
      {formatDate(event.startTime)}
      <br />
      <strong>End:</strong>
      {formatDate(event.endTime)}
      <br />
    </div>
    <div class="priceAndQuantity">
      {#each groupTicketsByClass(purchasable.tickets) as ticket}
        {ticket.quantity} &times; ${ticket.price} – {ticket.ticketClass}
        <br />
      {/each}
    </div>
  </div>
  {#if !purchased}
    <div class="removeButtonWrapper">
      <button on:click={removeFromCart}>Remove</button>
    </div>
  {/if}
</div>
