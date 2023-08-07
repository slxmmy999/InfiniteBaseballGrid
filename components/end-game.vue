<template>
  <div v-if="gameOver" :class="$style.popup">
    <div :class="$style.container">
      <h2 :class="$style.title">Game Over</h2>
      <p :class="$style.text">You scored {{ $store.state.score }} points!</p>
      <!-- Add grid with top player answers for each space -->
      <button :class="$style['popup-button']" @click="newGame()">Play Again</button>
      <button :class="$style['popup-button']" @click="goToMenu()">Main Menu</button>
    </div>
  </div>
</template>

<style module>
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0,0,0,0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.container {
  background-color: #202020;
  border-radius: 15px;
  padding: 30px;
  max-width: 90%;
  width: 500px;
  box-sizing: border-box;
  text-align: center;
}

.grid {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.row {
  display: flex;
  flex-direction: row;
}

.cell {
  width: 30px;
  height: 30px;
  margin: 1px;
  border-radius: 5px;
  background-color: #202020;
}

.cell_inner {
  width: 100%;
  height: 100%;
  border-radius: 5px;
}

.title {
  color: white;
  font-family: 'Roboto', sans-serif;
  font-size: 30px;
  margin-bottom: 20px;
}

.text {
  color: white;
  font-family: 'Roboto', sans-serif;
  font-size: 20px;
  margin-bottom: 30px;
  text-align: center;
}

.popup-button {
  color: white;
  font-family: 'Roboto', sans-serif;
  font-size: 20px;
  padding: 10px 20px;
  margin: 10px;
  background-color: red;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.popup-button:hover {
  background-color: #ff1a1a;
}
</style>

<script>
import { EventBus } from '../event-bus.js'

export default {
  data () {
    return {
      gameOver: false
    }
  },
  created () {
    EventBus.$on('game-over', () => {
      this.gameOver = true
    })
  },
  methods: {
    newGame () {
      parent.location.reload()
    },
    goToMenu () {
      this.gameOver = false
    }
  }
}
</script>
