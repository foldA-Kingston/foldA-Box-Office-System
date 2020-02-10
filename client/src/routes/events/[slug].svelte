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
  .heading {
		font-family: "Verdana", sans-serif;
		font-size: 30px;
		color: rgba(64, 69, 237);
		font-weight: bolder;
  }  

  .panel{
		width: 800px;
    height: 350px;
    border-radius: 10px;
    overflow: hidden;
    margin: 1rem 0.5rem;
	  position: relative;
    background-color:  rgba(64, 69, 237);
    color: white;

	}
  .twoColumns {
    display: flex;
  }

  table {
    margin: 1rem 0.5rem;
    position: relative;
	  border-collapse: collapse;
    box-shadow: 2px 2px 5px rgb(131, 131, 131);
  }
  .tableheader {
    background-color: rgb(228, 228, 228); 
  }
  td {
    border: solid rgb(77, 77, 77) 0.5mm;
	  border-collapse: collapse;
  }
  .eventimg {
	  float: left;
	  clear: left;
    height: 300px;
    width: 400px;
    border-radius: 10px;
    padding: 10px;
  }
  .scrollable{
   overflow: auto;
   width: 70px; /* adjust this width depending to amount of text to display */
   height: 50px; /* adjust height depending on number of options to display */
   border: 1px silver solid;
 }
 .scrollable select{
   border: none;
 }

</style>

<svelte:head>
  <title>{event.name}</title>
</svelte:head>

<h1 class = "heading">{event.name}</h1>


<div class="twoColumns">
<div class ="panel"> 
  <img class = "eventimg" alt='Event Photo' src={event.src} width="500" height="400">
  <br /> 
  <p>
    Date: {event.date}
    <br /> 
    Artist: {event.artist}
  </p>
</div>
  
    <table style="width:50%">
		 <tr>
            <td class= "tableheader">Type</td>
            <td class= "tableheader">Price</td>
            <td class= "tableheader">Quantity</td>
    </tr>
    <tr>
        <td>General</td>
        <td>$40</td>
        <div class="scrollable">
          <select size="6" multiple="multiple">
              <option value="1" selected>1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
          </select>
       </div>
			
    </tr>
		<tr> 
		 	<td>Student</td>
      <td>$30</td>
      <div class="scrollable">
          <select size="6" multiple="multiple">
              <option value="1" selected>1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
          </select>
       </div>
		</tr>
    <tr>
      <button style= "padding: 3px;" onclick="window.location.href = '/Cart'">Add To Cart</button>
    </tr>
    </table>
</div>




