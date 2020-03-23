<script>
  export let title;
</script>

<style>
  .panel {
    width: 100%;
    border-radius: 4px;
    border: 1px solid #333;
    margin: 1rem 0.5rem;
  }

  .panel h3 {
    width: 100%;
    padding: 1rem;
    background-color: var(--offwhite);
    border-bottom: 1px solid #333;
  }

  .panel .content {
    padding: 1rem;
  }
</style>

<div class="panel">
  <h3>{title}</h3>
  <div class="content">
    <slot />
  </div>
</div>
