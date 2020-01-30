<script>
    import Panel from "../components/Panel.svelte";
    let cart = [
    {
      name: "Movie 1",
      artist: "Ann Doe",
      time: "9:00 AM"
    },
    {
      name: "Movie 2",
      artist: "John Lennon",
      time: "10:00 AM"
    }
  ];
</script>

<style>
  .headingWrapper {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
  .headingWrapper > * {
    margin: 0;
  }

  .twoColumns {
    display: flex;
  }

  .checkBox {
	  margin-left: 1rem;
	  padding-right: 1rem;
  }

  .dayEvent {
    display: flex;
    margin: 1rem 0;
    align-items: center;
  }

  .dayEvent .imgPlaceholder {
    height: 5rem;
    width: 5rem;
    border-radius: 50%;
    border: 2px solid #555;
    background-color: var(--offwhite);
    margin-right: 1rem;
  }

  .dayEventHeading {
    display: flex;
    font-size: 1.4rem;
    align-items: center;
  }
  .dayEventHeading h4 {
    margin: 0;
    padding: 0;
    font-weight: bold;
    text-decoration: underline;
  }

  .dayEventHeading time {
    margin: 0;
    padding: 0;
    margin-left: 2rem;
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

  table, td {
	  border: solid black 0.5mm;
	  border-collapse: collapse;
  }
</style>

<svelte:head>
  <title>Cart</title>
</svelte:head>
<div class="headingWrapper">
  <h1>Day Passes</h1>
</div>

<div class="twoColumns">
  <Panel title="Select">
    {#each cart as item}
      <div class="dayEvent">
	  	<div class="checkBox">
		  <form>
			<input type="checkbox" name="Event1" value="Event Name">
		  </form>
	    </div>
        <div class="imgPlaceholder" />
        <div>
          <div class="dayEventHeading">
            <h4>{item.name}</h4>
            <time>{item.time}</time>
          </div>
          <div class="artistName">{item.artist}</div>
        </div>
        <div class="removeButtonWrapper">
          <button>Remove</button>
        </div>
      </div>
    {/each}
  </Panel>
  <Panel title="Schedule">
        <table>
            <tr>
                <td>Time</td>
                <td>Event</td>
            </tr>
            <tr>
                <td>9:00 AM</td>
                <td>Ann Doe</td>
            </tr>
        </table>
  </Panel>
</div>
