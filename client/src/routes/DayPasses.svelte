<script>
	import Panel from "../components/Panel.svelte";
	let cart = [
    {
      name: "Event Name",
      artist: "Ann Doe",
      time: "9:00 AM"
    },
    {
      name: "Event name",
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

  .headingWrapper > button {
    margin-left: 1rem;
  }

  .twoColumns {
    display: flex;
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
    margin-left: 1rem;
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
</style>

<svelte:head>
	<title>Day Pass</title>
</svelte:head>

<div class="headingWrapper">
  <h1>Day Passes</h1>
</div>

<div class="twoColumns">
	<panel title="Select">
		{#each cart as item}
		<div class="dayEvent">
			<div class="imgPlaceholder"></div>
			<div>
				<div class="dayEventHeading">
					<h4>{item.name}</h4>
					<time datetime={item.time}>{item.time}</time>
				</div>
				<div class="artistName"></div>
			</div>
			<div class="removeButtonWrapper">
				<button>Remove</button>
			</div>
		</div>	
		{/each}
	</panel>
	<pane; title="Schedule">
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
	</pane>
</div>