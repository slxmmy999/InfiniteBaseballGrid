<template>
  <div v-if="showBanner" class="banner">
    <div class="banner-content">
      <h1>Help me keep the site ad free! (and also feed me)</h1>
      <p>I am a college student working two jobs just to pay rent and feed myself. All of your <a href="https://allmylinks.com/sam-coan">donations</a> ensure I can keep the site ad free and also not be homeless! Thank you!</p>
      <button @click="closeBanner" class="close-button">Shut up nerd</button>
    </div>
  </div>
</template>

<script>
import Cookies from 'js-cookie'

export default {
  data () {
    return {
      showBanner: false
    }
  },
  mounted () {
    if (Cookies.get('visited') && !Cookies.get('begged_for_cash')) {
      this.showBanner = true
    }
  },
  methods: {
    closeBanner () {
      this.showBanner = false
      Cookies.set('begged_for_cash', 'true', { expires: 365 })
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

@media screen and (max-width: 768px) {
  .banner-content {
    flex-direction: column;
    max-width: 300px !important;
  }
}

.banner-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.banner-content p, .banner-content h1 {
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
