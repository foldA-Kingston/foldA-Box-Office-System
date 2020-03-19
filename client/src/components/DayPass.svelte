<script>
  import Panel from "./Panel.svelte";
  export let purchasable;
  let events = purchasable.events;
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

<Panel title={`Day pass: ${purchasable.description}`}>
  <div class="panelContent">
    <div class="thumbnail">
      <img src="event2.png" alt={purchasable.description} />
    </div>
    <div>
      <div class="eventHeading">
        <h2>{purchasable.description}</h2>
        <div>&bull;</div>
        <time datetime={purchasable.startTime}>{purchasable.startTime}</time>
      </div>
      <div class="artistName">
        Artists: {[...new Set(events.map(e => e.artistName))].join(', ')}
      </div>
      <div>Includes {events.length} events</div>
    </div>
    <div class="buttonWrapper">
      <a class="button" href="/todo">Buy Day Pass</a>
    </div>
  </div>
</Panel>
