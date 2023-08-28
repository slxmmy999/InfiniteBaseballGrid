<template>
  <div>
    <notification-banner v-if="showBanner" @close="closeBanner" />
    <top-menu />
    <game-grid :class="$style.grid" />
    <SearchDialog />
    <welcome-screen />
    <share-popup />
    <end-game />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      showBanner: false
    }
  },

  methods: {
    closeBanner () {
      this.showBanner = false
    }
  },
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
