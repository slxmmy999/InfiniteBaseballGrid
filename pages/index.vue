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
    this.$gtag('config', 'UA-131755589-1', {
      page_path: this.$route.path
    })
  }
}
</script>

<style module>
  .grid {
    margin-top: 3%;
  }
</style>
