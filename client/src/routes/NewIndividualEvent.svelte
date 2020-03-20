<script>
  import { goto } from "@sapper/app";
  import { jwt } from "../stores.js";
  import Flatpickr from "svelte-flatpickr";

  import "flatpickr/dist/flatpickr.css";
  import "flatpickr/dist/themes/light.css";

  let artistName = "";
  let imageUrl = null;
  let embedMedia = null;
  let description = "";
  let startTime = null;
  let endTime = null;
  let venue = "";
  let capacity = 0;
  let name = "";

  const flatpickrOptions = {
    enableTime: true,
    onChange: (selectedDates, dateStr, instance) => {
      console.log("Options onChange handler");
    }
  };

  function changeStartTime(selectedDates, dateStr, instance) {
    console.log("Svelte onChange handler");
  }

  $: handleCreate = () => {
    fetch("http://localhost:5000/events/", {
      mode: "cors",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      },
      body: JSON.stringify({
        artistName,
        imageUrl,
        embedMedia,
        description,
        startTime,
        endTime,
        venue,
        capacity,
        name
      })
    }).then(r => {
      if (r.ok) {
        const id = 1;
        goto(`/individual-events/${id}`);
      } else {
        alert("Something went wrong. Please try again in a moment.");
      }
    });
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
  .inputField,
  .confirm {
    padding: 0.5rem 1rem;
  }

  .ticketClassWrapper {
    border: 1px solid #ddd;
    padding: 0.5rem;
    margin: 0.5rem;
    background-color: #fafafa;
    border-radius: 4px;
  }
</style>

<svelte:head>
  <title>New Individual Event</title>
</svelte:head>
<div>
  <h1>New Individual Event</h1>
</div>
<div class="panel">
  <div class="inputField">
    <h3>Event Name</h3>
    <input bind:value={name} />
  </div>
  <div class="inputField">
    <h3>Description</h3>
    <input bind:value={description} />
  </div>
  <div class="inputField">
    <h3>Artist Name</h3>
    <input bind:value={artistName} />
  </div>
  <div class="inputField">
    <h3>Image URL</h3>
    <input bind:value={imageUrl} />
  </div>
  <div class="inputField">
    <h3>Embedded media (e.g. YouTube video)</h3>
    <input bind:value={embedMedia} />
  </div>
  <div class="inputField">
    <h3>Start date / time</h3>
    <Flatpickr
      options={flatpickrOptions}
      bind:value={startTime}
      placeholder="Start time" />
  </div>
  <div class="inputField">
    <h3>End date / time</h3>
    <Flatpickr
      options={flatpickrOptions}
      bind:value={endTime}
      placeholder="End time" />
  </div>
  <div class="inputField">
    <h3>Venue</h3>
    <input bind:value={venue} />
  </div>
  <div class="inputField">
    <h3>Capacity</h3>
    <input type="number" bind:value={capacity} />
  </div>
  <div class="ticketClassWrapper">
    <h3>Ticket Classes</h3>
    <em>Select box here</em>
    <br />
    <button>Create new ticket class</button>
  </div>

  <div class="confirm">
    <button class="create" on:click={handleCreate}>
      <h3>Create Event</h3>
    </button>
  </div>
</div>
