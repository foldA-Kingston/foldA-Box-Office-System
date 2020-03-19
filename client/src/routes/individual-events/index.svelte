<script>
  export let events = [];

  function sortByArtist() {
    for (let i = 0; i < events.length; i++) {
      for (let j = i + 1; j < events.length; j++) {
        if (events[i].artist > events[j].artist) {
          let temp = events[i];
          events[i] = events[j];
          events[j] = temp;
        }
      }
    }
  }
  function sortByName() {
    for (let i = 0; i < events.length; i++) {
      for (let j = i + 1; j < events.length; j++) {
        if (events[i].name > events[j].name) {
          let temp = events[i];
          events[i] = events[j];
          events[j] = temp;
        }
      }
    }
  }
</script>

<style>
  .events {
    display: block;
  }
  .heading {
    font-family: "Poppins";
    font-size: 40px;
    color: rgba(64, 69, 237);
    font-weight: bolder;
    display: inline;
  }
  p {
    position: relative;
    display: block;
  }
  .eventheading {
    text-decoration: none;
    text-shadow: 1px 1px gray;
    font-weight: bold;
    font-family: "Verdana", sans-serif;
    font-size: 20px;
    color: rgba(64, 69, 237);
  }
  .panel {
    width: 100%;
    border-radius: 10px;
    border: 2px solid rgb(61, 61, 61);
    overflow: hidden;
    margin: 1rem 0.5rem;
    position: relative;
  }
  .buttonwrapper {
    position: absolute;
    bottom: 45%;
    right: 20px;
    display: flex;
    justify-content: flex-end;
    flex-grow: 1;
  }
  .eventimg {
    float: left;
    clear: left;
  }

  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
  }
  .options {
    color: black;
    background-color: #f1f1f1;
    padding: 12px 16px;
    min-width: 160px;
    z-index: 1;
    text-align: left;
  }

  .dropdown:hover .dropdown-content {
    display: block;
  }
  .dropdown-content button:hover {
    background-color: rgb(184, 184, 184);
  }
</style>

<svelte:head>
  <title>Events</title>
</svelte:head>
<h1 class="heading">
  EVENTS
  <div class="dropdown">
    <button class="scrolldownbutton">Sort</button>
    <div id="myOptions" class="dropdown-content">
      <button class="options" on:click={() => sortByArtist()}>artist</button>
      <button class="options" on:click={() => sortByName()}>name</button>
      <button class="options">something else</button>
    </div>
  </div>

</h1>
<div class="events">
  {#each events as event}
    <div class="panel">
      <img
        class="eventimg"
        alt="Event Photo"
        src={event.src}
        width="250"
        height="200" />
      <h class="eventheading">
        <a style="text-decoration: none;" href="events/{event.slug}">
          {event.name}
        </a>
      </h>

      <br />
      <p>
        Date: {event.date}
        <br />
        Artist: {event.artist}
      </p>
      <div class="buttonwrapper">
        <button onclick="window.location.href = 'events/{event.slug}';">
          Buy Tickets
        </button>
      </div>
    </div>
  {/each}
</div>
