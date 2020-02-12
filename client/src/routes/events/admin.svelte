<script context="module">
	export function preload({ params, query }) {
		return this.fetch(`events.json`).then(r => r.json()).then(events => {
			return { events };
		});
	}
</script>

<script>
    export let events;
    function changeDate() {
        {events[0].date ="APRIL 26"}
    }
</script>
<button on:click={changeDate}>Click here to chaneg the date</button>

