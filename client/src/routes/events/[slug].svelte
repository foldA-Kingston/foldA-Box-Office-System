<script context="module">
  export async function preload({ params, query }) {
    // the `slug` parameter is available because
    // this file is called [slug].svelte
    const res = await this.fetch(`events/${params.slug}.json`);
    const data = await res.json();

    if (res.status === 200) {
      return { event: data };
    } else {
      this.error(res.status, data.message);
    }
  }
</script>

<script>
  export let event;
</script>

<style>
  
  .twoColumns {
    display: flex;
  }

  table, td {
	  border: solid black 0.5mm;
	  border-collapse: collapse;
  }
</style>

<svelte:head>
  <title>{event.name}</title>
</svelte:head>

<h1>{event.name}</h1>


<div class="twoColumns">
  <img alt='Event Photo' src={event.src} width="500" height="400">
  
    <table style="width:50%">
		 <tr>
            <td>Type</td>
            <td>Price</td>
        </tr>
        <tr>
            <td>General</td>
            <td>$40</td>
			
        </tr>
		<tr> 
		 	<td>Student</td>
            <td>$30</td>
		</tr>
    </table>
</div>




