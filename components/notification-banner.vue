<template>
    <div v-if="showBanner" class="banner">
      <div class="banner-content">
        <p>Our site name has changed from <strong style="color: red;">Infinite Immaculate Grid</strong> to <strong style="color:  #228B22;"><u>Infinite Baseball Grid</u></strong>. Please update your bookmarks to <a style="color: #228B22;" href="https://www.infinitebaseballgrid.com">www.infinitebaseballgrid.com</a>.</p>
        <button @click="closeBanner" class="close-button">Close</button>
      </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      showBanner: true
    }
  },
  methods: {
    closeBanner () {
      this.showBanner = false
    }
  }
}
</script>

<style scoped>
.banner {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #f4b836;
  color: white;
  z-index: 999;
  text-align: center;
  padding: 10px;
}

.banner-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.banner-content p {
  margin: 0;
  font-size: 16px;
  font-family: 'Roboto', sans-serif;
}

.banner-content a {
  color: #fff;
  text-decoration: underline;
}

.close-button {
  background-color: #f4b836;
  cursor: pointer;
  border: 2px solid #f0f0f0;
  border-radius: 4px;
  font-size: 20px;
  line-height: 1;
  color: white;
  padding: 5px 10px;
  font-family: 'Roboto', sans-serif;
}

.close-button:hover {
  color: #f0f0f0;
}
</style>
