<svelte:head>
	<title>Events</title>
</svelte:head>
<script>
 	import Panel from "../components/Panel.svelte";
	let events = [
		{name: 'event1', date: 'April 1', src: 'great-success.png'},
		{name: 'event2', date: 'June 2', src: 'favicon.png'},
		{name: 'event3', date: 'June 14', src: 'logo-192.png'}
		];
</script>
<style>
    .events {
		display: block;
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
<h1>Events</h1>
<div class = "events">
	{#each events as event}
		<Panel title={event.name}>
		<img alt='Event Photo' src={event.src} width="200" height="200">
		<p>{event.name} <br> Date: {event.date}</p>
		<button>Buy Tickets</button>
		</Panel>
		
	{/each}
</div>
