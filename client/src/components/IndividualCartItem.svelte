<script>
  export let purchasable;
  export let groupTicketsByClass;
</script>

<style>
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
      <h4>{purchasable.name}</h4>
    </div>
    <div class="artistName">{purchasable.artists}</div>
    <div class="priceAndQuantity">
      {#each groupTicketsByClass(purchasable.tickets) as ticket}
        {ticket.quantity} &times; {ticket.price} – {ticket.ticketClass}
        <br />
      {/each}
    </div>
  </div>
  <div class="removeButtonWrapper">
    <button>Remove</button>
  </div>
</div>
