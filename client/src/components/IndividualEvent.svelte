<script>
  import Panel from "./Panel.svelte";
  export let purchasable;
  let event = purchasable.events[0];
</script>

<style>
  .panelContent {
    display: flex;
  }

  .panelContent > * {
    margin: 0 0.5rem;
  }

  .thumbnail {
    border-radius: 50%;
    overflow: hidden;
    width: 10rem;
    height: 10rem;
    margin-right: 1.5rem;
  }

  .thumbnail img {
    height: 100%;
    width: 100%;
  }

  .eventHeading {
    display: flex;
    align-items: center;
    height: 3em;
  }

  .eventHeading > * {
    margin: 0;
    padding: 0;
    padding-right: 0.5rem;
    display: block;
  }

  .artistName {
    margin-bottom: 0.75rem;
    font-style: italic;
  }

  .buttonWrapper {
    display: flex;
    align-items: center;
  }
</style>

{#if event}
  <Panel title={`Single event: ${purchasable.name}`}>
    <div class="panelContent">
      <div class="thumbnail">
        <img src="event2.png" alt={event.name} />
      </div>
      <div>
        <div class="eventHeading">
          <h2>{event.name}</h2>
          <div>&bull;</div>
          <time datetime={event.startTime}>{event.startTime}</time>
        </div>
        <div class="artistName">{event.artistName}</div>
        <div>{event.description}</div>
      </div>
      <div class="buttonWrapper">
        <a class="button" href={`/individual-events/${event.id}`}>
          Buy Tickets
        </a>
      </div>
    </div>
  </Panel>
{:else}
  <div>Error: no event for purchasable {purchasable.id}</div>
{/if}
