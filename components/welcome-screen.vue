<template>
    <div class="welcome-screen" v-if="showWelcome">
      <div class="content">
        <h1>Welcome to Infinite Immaculate Grid!</h1>
        <p>
          This website is a work in progress. We are currently working on adding more features and improving the existing ones. If you have any suggestions, please let us know!
          If you are interested in the project check out the <a href="https://github.com/slxmmy999/InfiniteImmaculateGrid">GitHub</a> page. You can also join the
          <a href="https://discord.gg/rPBuvhqG8p">Discord</a> server to get updates on the project and chat with other users, or follow me on <a href="https://twitter.com/slxmmy999">Twitter</a>.
        </p>
        <button @click="closeWelcome">Got it!</button>
      </div>
    </div>
</template>

<script>
import Cookies from 'js-cookie'

export default {
  data () {
    return {
      showWelcome: false
    }
  },
  mounted () {
    if (!Cookies.get('visited')) {
      this.showWelcome = true
    }
  },
  methods: {
    closeWelcome () {
      this.showWelcome = false
      Cookies.set('visited', 'true', { expires: 365 }) // This cookie will expire in 1 year
    }
  }
}
</script>

<style scoped>
.welcome-screen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0,0,0,0.7);
  z-index: 1000;
}

.content {
  background: #202020;
  border-radius: 15px;
  padding: 30px;
  max-width: 90%;
  width: 500px;
  box-sizing: border-box;
  text-align: center;
}

.content h1 {
  color: #fff;
  margin-bottom: 20px;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.content p {
  color: #bbb;
  margin-bottom: 30px;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.content button {
  background: #4a90e2;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.content button:hover {
  background: #357ac9;
}
</style>
