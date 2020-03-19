<script context="module">
  export async function preload(page, session) {
    const { slug } = page.params;

    const res = await this.fetch(`http://localhost:5000/events/${slug}/`, {
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    });
    const event = await res.json();

    return { event };
  }
</script>

<script>
  export let event = {};

  let cartItems = [];

  var generalOption = 0; //option id 1
  var studentOption = 0; //option id 2

  function handleClick(id, opID) {
    if (opID == 1) {
      generalOption = id;
    } else if (opID == 2) {
      studentOption = id;
    }
  }

  function addToCart(event) {
    cartItems.push({ name: "Hello", date: "date", artist: "bob", num: 5 });
  }
</script>

<style>
  .heading {
    font-family: "Verdana", sans-serif;
    font-size: 30px;
    color: rgba(64, 69, 237);
    font-weight: bolder;
  }

  .panel {
    width: 800px;
    height: 350px;
    border-radius: 10px;
    overflow: hidden;
    margin: 1rem 0.5rem;
    position: relative;
    background-color: rgba(64, 69, 237);
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
  .scrolldownbutton {
    color: black;
    text-align: left;
    border-color: rgb(70, 70, 70) 1mm;
    border-radius: 10px;
    background-color: white;
    padding: 16px;
  }
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
  }
  .dropdown-content button {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .options {
    background-color: #f1f1f1;
    padding: 12px 16px;
    min-width: 160px;
    z-index: 1;
    text-align: left;
  }
  .description {
    font-size: 10px;
    padding: 10px;
  }

  .dropdown:hover .dropdown-content {
    display: block;
  }

  .dropdown:hover .scrolldownbutton {
    background-color: #e6e6e6;
  }

  .dropdown-content button:hover {
    background-color: rgb(184, 184, 184);
  }
</style>

<svelte:head>
  <title>{event.name}</title>
</svelte:head>

<h1 class="heading">{event.name}</h1>
<code>{JSON.stringify(event)}</code>
<div class="twoColumns">
  <div class="panel">
    <img
      class="eventimg"
      alt="Event Photo"
      src={event.imageUrl}
      width="500"
      height="400" />

    <p>
      Date: {event.startTime}
      <br />
      Artist: {event.artistName}
    </p>
    <div class="description">{event.description}</div>

  </div>

  <table style="width:50%">
    <tr>
      <td class="tableheader">Type</td>
      <td class="tableheader">Price</td>
      <td class="tableheader">Quantity</td>
    </tr>
    <tr>
      <td>General</td>
      <td>$40</td>
      <td>
        <div class="dropdown">
          <button class="scrolldownbutton">
            {generalOption}
            <img style="float: right;" alt="scroll" src="scroll.png" />
          </button>
          <div class="dropdown-content">
            <button class="options" on:click={() => handleClick('1', 1)}>
              1
            </button>
            <button class="options" on:click={() => handleClick('2', 1)}>
              2
            </button>
            <button class="options" on:click={() => handleClick('3', 1)}>
              3
            </button>
            <button class="options" on:click={() => handleClick('4', 1)}>
              4
            </button>
            <button class="options" on:click={() => handleClick('5', 1)}>
              5
            </button>
          </div>
        </div>
      </td>

    </tr>
    <tr>
      <td>Student</td>
      <td>$30</td>
      <td>
        <div class="dropdown">
          <button class="scrolldownbutton">
            {studentOption}
            <img style="float: right;" alt="scroll" src="scroll.png" />
          </button>
          <div class="dropdown-content">
            <button class="options" on:click={() => handleClick('1', 2)}>
              1
            </button>
            <button class="options" on:click={() => handleClick('2', 2)}>
              2
            </button>
            <button class="options" on:click={() => handleClick('3', 2)}>
              3
            </button>
            <button class="options" on:click={() => handleClick('4', 2)}>
              4
            </button>
            <button class="options" on:click={() => handleClick('5', 2)}>
              5
            </button>
          </div>
        </div>
      </td>
    </tr>
    <tr>
      <td>
        <button onclick="window.location.href = '/Cart'">Add To Cart</button>
      </td>
    </tr>
  </table>
</div>
