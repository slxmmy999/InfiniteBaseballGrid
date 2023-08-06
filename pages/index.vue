<template>
  <div>
    <head>
      <script>
        if (top !== self) top.location.replace(self.location.href);
      </script>
    </head>
    <top-menu />
    <game-grid :class="$style.grid" />
    <SearchDialog />
    <welcome-screen />
    <share-popup />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  // send a Google Analytics page view on page load
  mounted () {
    this.$gtm.trackView('/')
  }
}
</script>

<style module>
  .grid {
    margin-top: 2%;
  }
</style>
