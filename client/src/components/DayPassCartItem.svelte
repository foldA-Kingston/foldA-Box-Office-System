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
    font-size: 1.3rem;
    align-items: center;
  }

  h4 {
    font-size: 1.2rem;
    font-weight: bold;
    margin-top: 0.8rem;
  }

  .cartItemHeading h3 {
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

  table.eventsList {
    width: 100%;
  }

  table.eventsList td,
  table.eventsList th {
    padding: 0.2rem;
    text-align: center;
  }

  .schedule {
    border: 1px solid #ddd;
    background-color: #fafafa;
    padding: 0.5rem;
    border-radius: 4px;
    margin: 1rem;
  }

  .schedule strong {
    font-size: 1.1rem;
  }
</style>

<div class="cartItem">
  <div class="imgPlaceholder" />
  <div>
    <div class="cartItemHeading">
      <h3>
        Day pass:
        <a href={`/day-passes/${purchasable.id}`}>{purchasable.name}</a>
      </h3>
    </div>
    <!-- {JSON.stringify(purchasable)} -->
    <div class="artistName">{purchasable.artists}</div>
    <div class="priceAndQuantity">
      {#each groupTicketsByClass(purchasable.tickets) as ticket}
        {ticket.quantity} &times; ${ticket.price} – {ticket.ticketClass}
        <br />
      {/each}
    </div>
    <div>
      <h4>Schedules:</h4>
      {#each purchasable.tickets as ticket}
        <div class="schedule">
          <strong>
            ${ticket.ticketClass.price} – {ticket.ticketClass.description}
          </strong>
          <br />
          <table class="eventsList">
            <thead>
              <tr>
                <th>Name</th>
                <th>Venue</th>
                <th>Start</th>
                <th>End</th>
              </tr>
            </thead>
            <tbody>
              {#each ticket.events as event}
                <tr>
                  <td>{event.name}</td>
                  <td>{event.venue}</td>
                  <td>{formatDate(event.startTime)}</td>
                  <td>{formatDate(event.endTime)}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      {/each}
    </div>
  </div>
  {#if !purchased}
    <div class="removeButtonWrapper">
      <button on:click={removeFromCart}>Remove</button>
    </div>
  {/if}
</div>
