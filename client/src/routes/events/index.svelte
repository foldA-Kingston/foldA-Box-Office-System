<script context="module">
	export function preload({ params, query }) {
		return this.fetch(`events.json`).then(r => r.json()).then(events => {
			return { events };
		});
	}
</script>

<script>
	export let events;
</script>


<svelte:head>
	<title>Events</title>
</svelte:head>

<style>
    .events {
		display: block;
    }
	.heading {
		font-family: "Poppins";
		font-size: 40px;
		color: rgba(64, 69, 237);
		font-weight: bolder;
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

</style>
<h1 class="heading">EVENTS</h1>
<div class = "events">
	{#each events as event}
	<div class="panel">
			<img class = "eventimg" alt='Event Photo' src={event.src} width="250" height="200">
			<h class = "eventheading"> 
			<a style ="text-decoration: none;" href='events/{event.slug}'>{event.name}</a>
			</h>
			
			<br /> 
			<p>
			Date: {event.date}
			<br /> 
			Artist: {event.artist}
			</p>
			<div class = "buttonwrapper">
				<button onclick="window.location.href = 'events/{event.slug}';">Buy Tickets</button>
			</div>
	</div>
	{/each}
</div>

