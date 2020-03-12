<script>
  import { onMount } from "svelte";
  import Panel from "../components/Panel.svelte";

  let events = [];

  onMount(async () => {
    const result = await fetch("http://localhost:5000/individualEvents/", {
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    });
    events = await result.json();
  });
</script>

<style>
  .events {
    display: block;
  }
  .heading {
    font-family: "Verdana", sans-serif;
    font-size: 40px;
    color: rgba(64, 69, 237);
  }

  .panelContent {
    display: flex;
  }

  .panelContent > * {
    padding: 0.5rem;
  }

  .imageWrapper {
    overflow: hidden;
    border-radius: 50%;
    height: 10rem;
    width: 10rem;
    padding: 0;
    margin: 0;
  }
  .imageWrapper img {
    height: 100%;
    width: 100%;
    display: block;
  }
</style>

<svelte:head>
  <title>Events</title>
</svelte:head>
<h1 class="heading">EVENTS</h1>
<div class="events">
  {#each events as event}
    <Panel title={event.description}>
      <div class="panelContent">
        <div class="imageWrapper">
          <img src="event2.png" alt={event.description} />
        </div>
        <div>
          <div>{event.description} &bull; {event.startDate}</div>
          <div class="artist">{event.artist}</div>
          <div>Longer description...</div>
        </div>
        <div>
          <button>Buy tickets</button>
        </div>
      </div>
    </Panel>
  {/each}
</div>
