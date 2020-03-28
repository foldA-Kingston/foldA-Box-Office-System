<script context="module">
  export async function preload(page, session) {
    const { slug } = page.params;

    return { slug };
  }
</script>

<script>
  export let slug;
  import { goto } from "@sapper/app";
  import { onMount } from "svelte";
  import { userId, jwt, isAdmin } from "../../stores.js";
  import { formatDate } from "../../utils.js";

  let event = {};
  const ticketSelection = {};

  onMount(async () => {
    const res = await fetch(`http://localhost:5000/events/${slug}/`, {
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    });
    event = await res.json();
    if (event.purchasable && event.purchasable.ticketClasses) {
      event.purchasable.ticketClasses.forEach(tc => {
        ticketSelection[tc.id] = 0;
      });
    }
  });

  $: addToCart = () => {
    Object.keys(ticketSelection).forEach(ticketClassId => {
      fetch(`http://localhost:5000/users/${$userId}/cart/`, {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${$jwt}`
        },
        body: JSON.stringify({
          purchasableId: event.purchasable.id,
          ticketClassId: Number(ticketClassId),
          quantity: ticketSelection[ticketClassId],
          events: [event.id]
        })
      }).then(r => {
        if (r.ok) {
          goto(`/Cart`);
        } else {
          alert("Something went wrong. Please try again in a moment.");
        }
      });
    });
  };

  $: deleteEvent = async () => {
    await fetch(`http://localhost:5000/purchasables/${event.purchasable_id}/`, {
      mode: "cors",
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      }
    });
    goto("/");
  };
</script>

<style>
  .date,
  .artist,
  .venue {
    padding: 0.2rem 1rem;
  }
  .heading {
    font-family: "Verdana", sans-serif;
    font-size: 1.6rem;
    color: rgba(64, 69, 237);
    font-weight: bolder;
  }

  .panel {
    width: 800px;
    height: 350px;
    border-radius: 10px;
    overflow: hidden;
    margin: 1rem 0.5rem;
    position: relative;
    background-color: rgba(64, 69, 237);
    color: white;
    display: flex;
    flex-wrap: wrap;
  }
  .twoColumns {
    display: flex;
  }

  table {
    margin: 1rem 0.5rem;
    position: relative;
    border-collapse: collapse;
    box-shadow: 2px 2px 5px rgb(131, 131, 131);
    width: 100%;
  }
  .tableheader {
    background-color: rgb(228, 228, 228);
  }
  td {
    border: solid rgb(77, 77, 77) 0.5mm;
    border-collapse: collapse;
  }
  .eventimg {
    border-radius: 10px;
    padding: 1rem;
    max-height: 100%;
    max-width: 100%;
  }

  .panelImg {
    height: 100px;
    width: 200px;
  }

  .description {
    padding: 1rem;
  }

  .deleteEvent {
    background-color: red;
  }
</style>

<svelte:head>
  <title>{event.name}</title>
</svelte:head>

<h1 class="heading">{event.name}</h1>
<div class="twoColumns">
  <div class="panel">
    <div class="panelImg">

      <img
        class="eventimg"
        alt="Event Photo"
        src={event.imageUrl}
        width="500"
        height="400" />
    </div>
    <div class="panelText">
      <div class="date">
        <strong>Date</strong>
        : {event.startTime && formatDate(event.startTime)}
      </div>
      <div class="artist">
        <strong>Artist</strong>
        : {event.artistName}
      </div>
      <div class="venue">
        <strong>Venue</strong>
        : {event.venue}
      </div>
      <div class="description">{event.description}</div>
    </div>
  </div>
  <div style="width:50%">
    <table>
      <thead>
        <tr>
          <th class="tableheader">Type</th>
          <th class="tableheader">Price</th>
          <th class="tableheader">Quantity</th>
        </tr>
      </thead>
      <tbody>
        {#if event && event.purchasable && event.purchasable.ticketClasses}
          {#each event.purchasable.ticketClasses as tc}
            <tr>
              <td>{tc.description}</td>
              <td>${tc.price}</td>
              <td>
                <input
                  type="number"
                  bind:value={ticketSelection[tc.id]}
                  on:change={() => {
                    ticketSelection = ticketSelection;
                  }} />
              </td>
            </tr>
          {/each}
        {/if}
      </tbody>
    </table>
    <button on:click={addToCart}>Add to cart</button>
  </div>
</div>
{#if isAdmin}
  <a class="button" href={`/edit-event/${event.id}`}>Edit event</a>
  <button on:click={deleteEvent} class="deleteEvent">Delete event</button>
{/if}
