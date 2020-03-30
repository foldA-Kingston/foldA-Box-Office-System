<script>
  import { goto } from "@sapper/app";
  import { onMount, onDestroy } from "svelte";
  import { jwt } from "../stores.js";
  import { formatDate } from "../utils.js";
  import Flatpickr from "svelte-flatpickr";
  import Select from "svelte-select";

  let selectedValue;

  import "flatpickr/dist/flatpickr.css";
  import "flatpickr/dist/themes/light.css";

  let description = "";
  let numTickets = 0;
  let name = "";
  let type = "dayPass";

  let eventInput = {
    artistName: "",
    imageUrl: "",
    embedMedia: "",
    description: "",
    startTime: null,
    endTime: null,
    venue: "",
    capacity: 0,
    name: ""
  };

  const events = [];

  const flatpickrOptions = {
    enableTime: true,
    onChange: (selectedDates, dateStr, instance) => {
      console.log("Options onChange handler");
    }
  };

  $: handleCreate = () => {
    fetch("http://localhost:5000/purchasables/", {
      mode: "cors",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${$jwt}`
      },
      body: JSON.stringify({
        numTickets,
        type,
        description,
        name,
        ticketClasses: selectedValue.map(tc => tc.value)
      })
    }).then(async r => {
      if (r.ok) {
        const result = await r.json();

        await Promise.all(
          events.map(
            async event =>
              await fetch("http://localhost:5000/events/", {
                mode: "cors",
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `Bearer ${$jwt}`
                },
                body: JSON.stringify({
                  ...event,
                  purchasableId: result.id
                })
              })
          )
        );

        goto(`/day-passes/${result.id}`);
      } else {
        alert("Something went wrong. Please try again in a moment.");
      }
    });
  };

  let ticketClassOptions;

  $: fetchTicketClasses = async () => {
    const res = await fetch(`http://localhost:5000/ticketClasses/`, {
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    });
    const ticketClasses = await res.json();
    ticketClassOptions = ticketClasses.map(tc => ({
      label: `${tc.description} – $${tc.price}`,
      value: tc.id
    }));
  };

  onMount(() => {
    fetchTicketClasses();
  });

  const createNewTicketClass = async () => {
    const description = prompt("Ticket class name:");
    const price = prompt("Ticket class price:");

    if (description && price) {
      await fetch("http://localhost:5000/ticketClasses/", {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${$jwt}`
        },
        body: JSON.stringify({
          description,
          price: Number(price)
        })
      }).then(r => {
        if (r.ok) {
          fetchTicketClasses();
        } else {
          alert("Something went wrong. Please try again in a moment.");
        }
      });
    }
  };

  let creatingEvent = false;

  const addEvent = () => {
    creatingEvent = true;
  };

  const saveEvent = () => {
    events.push({
      ...eventInput
    });
    eventInput = {
      artistName: "",
      imageUrl: null,
      embedMedia: null,
      description: "",
      startTime: null,
      endTime: null,
      venue: "",
      capacity: 0,
      name: ""
    };
    creatingEvent = false;
  };
</script>

<style>
  .panel {
    border-radius: 4px;
    border: 1px solid #333;
    margin: 1rem 0.5rem;
    padding: 0.5rem;
  }
  .inputField,
  .confirm {
    padding: 0.5rem 1rem;
  }

  .ticketClassWrapper,
  .eventsWrapper {
    border: 1px solid #ddd;
    padding: 0.5rem;
    margin: 0.5rem;
    background-color: #fafafa;
    border-radius: 4px;
  }

  .eventsWrapper table {
    background-color: white;
    border-radius: 4px;
    border: 1px solid #ddd;
  }

  .eventsWrapper table td,
  .eventsWrapper table th {
    padding: 0.2rem;
  }
</style>

<svelte:head>
  <title>New Day Pass</title>
</svelte:head>
<div>
  <h1>New Day Pass</h1>
</div>
<div class="panel">
  <div class="inputField">
    <h3>Day pass Name</h3>
    <input bind:value={name} />
  </div>
  <div class="inputField">
    <h3>Description</h3>
    <input bind:value={description} />
  </div>
  <div class="inputField">
    <h3>Tickets available</h3>
    <input type="number" bind:value={numTickets} />
  </div>
  <div class="ticketClassWrapper">
    <h3>Ticket Classes</h3>
    {#if ticketClassOptions}
      <Select items={ticketClassOptions} isMulti bind:selectedValue />
    {/if}
    <br />
    <button on:click={createNewTicketClass}>Create new ticket class</button>
  </div>
  <div class="eventsWrapper">
    {#if creatingEvent}
      <div class="inputField">
        <h3>Event Name</h3>
        <input bind:value={eventInput.name} />
      </div>
      <div class="inputField">
        <h3>Description</h3>
        <input bind:value={eventInput.description} />
      </div>
      <div class="inputField">
        <h3>Artist Name</h3>
        <input bind:value={eventInput.artistName} />
      </div>
      <div class="inputField">
        <h3>Image name</h3>
        <input bind:value={eventInput.imageUrl} />
      </div>
      <div class="inputField">
        <h3>Embedded media (e.g. YouTube video)</h3>
        <input bind:value={eventInput.embedMedia} />
      </div>
      <div class="inputField">
        <h3>Start date / time</h3>
        <Flatpickr
          options={flatpickrOptions}
          bind:value={eventInput.startTime}
          placeholder="Start time" />
      </div>
      <div class="inputField">
        <h3>End date / time</h3>
        <Flatpickr
          options={flatpickrOptions}
          bind:value={eventInput.endTime}
          placeholder="End time" />
      </div>
      <div class="inputField">
        <h3>Venue</h3>
        <input bind:value={eventInput.venue} />
      </div>
      <div class="inputField">
        <h3>Capacity</h3>
        <input type="number" bind:value={eventInput.capacity} />
      </div>
      <button on:click={saveEvent}>Save event</button>
    {:else}
      <h3>Included events</h3>
      <table>
        <thead>
          <th>Name</th>
          <th>Desc.</th>
          <th>Artist</th>
          <th>Start</th>
          <th>End</th>
          <th>Venue</th>
          <th>Capacity</th>
        </thead>
        <tbody>
          {#each events as event}
            <tr>
              <td>{event.name}</td>
              <td>{event.description}</td>
              <td>{event.artistName}</td>
              <td>{formatDate(event.startTime)}</td>
              <td>{formatDate(event.endTime)}</td>
              <td>{event.venue}</td>
              <td>{event.capacity}</td>
            </tr>
          {/each}
        </tbody>
      </table>
      <button on:click={addEvent}>Add event to day pass</button>
    {/if}
  </div>
  <div class="confirm">
    <button class="create" on:click={handleCreate}>
      <h3>Create Day Pass</h3>
    </button>
  </div>
</div>
