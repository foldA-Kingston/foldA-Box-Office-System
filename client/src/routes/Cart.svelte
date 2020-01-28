<script>
  import Panel from "../components/Panel.svelte";
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
</style>

<svelte:head>
  <title>Cart</title>
</svelte:head>
<div class="headingWrapper">
  <h1>Checkout</h1>
  <button>Add More</button>
</div>

<div class="twoColumns">
  <Panel title="Cart">left</Panel>
  <Panel title="Total">right</Panel>
</div>
