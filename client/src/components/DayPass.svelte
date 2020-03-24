<script>
  import { formatDate } from "../utils.js";
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
    font-style: italic;
  }

  .desc,
  .artistName {
    margin-bottom: 0.75rem;
  }

  .buttonWrapper {
    display: flex;
    align-items: center;
  }
</style>

<Panel title={`Day pass: ${purchasable.name}`}>
  <div class="panelContent">
    <div class="thumbnail">
      <img src="event2.png" alt={purchasable.name} />
    </div>
    <div>
      <div class="eventHeading">
        <h2>
          <a href={`day-passes/${purchasable.id}`}>{purchasable.name}</a>
        </h2>
        <div>&bull;</div>
        First event at&nbsp;
        <time datetime={purchasable.startTime}>
          {formatDate(purchasable.startTime)}
        </time>
      </div>
      <div class="artistName">
        Artists: {[...new Set(events.map(e => e.artistName))].join(', ')}
      </div>
      <div class="desc">{purchasable.description}</div>
      <div class="desc">Includes {events.length} events</div>
    </div>
    <div class="buttonWrapper">
      <a class="button" href={`/day-passes/${purchasable.id}`}>Buy Tickets</a>
    </div>
  </div>
</Panel>
