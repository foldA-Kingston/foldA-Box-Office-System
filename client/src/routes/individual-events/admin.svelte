<script>
  export let events;
  function changeDate() {
    {
      events[0].date = "APRIL 26";
    }
  }
</script>

<button on:click={changeDate}>Click here to change the date</button>
