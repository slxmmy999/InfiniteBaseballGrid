<template>
  <div>
    <top-menu />
    <game-grid :class="$style.grid" />
    <SearchDialog />
  </div>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style module>
  .grid {
    margin-top: 3%;
  }
</style>
