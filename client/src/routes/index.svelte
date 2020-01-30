<svelte:head>
	<title>Events</title>
</svelte:head>
<script>
 	import Panel from "../components/Panel.svelte";
	let events = [
		{name: 'HowlRound Digital + Performance Convening', date: 'April 1', src: 'event1.png'},
		{name: 'Choir!Choir!Choir!', date: 'June 2', src: 'event2.png'},
		{name: 'event3', date: 'June 14', src: 'great-success.png'}
		];
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
	p {
		vertical-align: top;
		display: inline; 
		position: absolute;
	}
	button {
		display: inline;
		vertical-align: center;
		position: relative;
		bottom: 100px;
  		left: 800px;

	}
</style>
<h1 class=heading>EVENTS</h1>
<div class = "events">
	{#each events as event}
		<Panel title={event.name}>
		<img alt='Event Photo' src={event.src} width="200" height="200">
		<p>{event.name} <br> Date: {event.date}</p>
		<button>Buy Tickets</button>
		</Panel>
		
	{/each}
</div>
