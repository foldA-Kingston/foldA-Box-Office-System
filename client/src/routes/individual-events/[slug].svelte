<script context="module">
  export async function preload(page, session) {
    const { slug } = page.params;

    return { slug };
  }
</script>

<script>
  export let slug;

  import { onMount } from "svelte";

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

  const addToCart = () => {
    // this is where you create tickets with isPurchased=false
    alert("do something");
  };
</script>

<style>
  .date,
  .artist {
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
        : {event.startTime}
      </div>
      <div class="artist">
        <strong>Artist</strong>
        : {event.artistName}
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
                <input type="number" bind:value={ticketSelection[tc.id]} />
              </td>
            </tr>
          {/each}
        {/if}
      </tbody>
    </table>
    <button on:click={addToCart}>Add to cart</button>
  </div>
</div>
