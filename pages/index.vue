<template>
  <div>
    <top-menu />
    <game-grid :class="$style.grid" />
    <SearchDialog />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  // send a Google Analytics page view on page load
  mounted () {
    this.$ga.page('/')
  }
}
</script>

<style module>
  .grid {
    margin-top: 3%;
  }
</style>
