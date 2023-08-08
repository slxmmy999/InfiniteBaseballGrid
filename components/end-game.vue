<template>
  <div v-if="gameOver" :class="$style.popup">
    <div :class="$style.container">
      <h2 :class="$style.title">Game Over</h2>
      <p :class="$style.text">You scored {{ $store.state.score }} points!</p>
      <button :class="$style['popup-button']" @click="newGame()">Play Again</button>
      <button :class="$style['popup-button']" @click="goToMenu()">Main Menu</button>
      <!-- Grid with top player answers for each space -->
      <div :class="$style.grid">
        <div v-for="(answer, idx) in topAnswersGrid.flat()" :key="idx" :class="$style.cell">
          <!--img :src="answer" :class="$style['player-image']" :alt="answer + ' photo'"-->
          <div :class="$style.playerName">{{ answer }}</div>
        </div>
      </div>
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
  justify-content: center;
  align-items: center;
  z-index: 999;
  overflow: auto;
  padding: 20px;
}

.container {
  background-color: #202020;
  border-radius: 15px;
  padding: 30px;
  max-width: 90%;
  width: 500px;
  box-sizing: border-box;
  text-align: center;
  max-height: 80vh;
  overflow-y: auto;
}
.grid {
  padding-top: 10%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin: auto;
}

.row {
  display: flex;
  flex-direction: row;
}

.cell {
  border-radius: 0px;
  aspect-ratio: 1/1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-color: #111;
  width: 90%;
  height: 90%;
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

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2px;
  margin: auto;
  width: 100%;
  max-width: 500px;
}

.row {
  display: flex;
}

.cell {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid #fff;
  padding: 10px;
}

.player-image {
  width: 50%;
  height: auto;
  object-fit: cover;
}

.playerName {
  color: #fff;
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  text-align: center;
}
</style>

<script>
import { EventBus } from '../event-bus.js'

export default {
  data () {
    return {
      gameOver: false,
      topAnswersGrid: []
    }
  },
  created () {
    EventBus.$on('game-over', async () => {
      this.gameOver = true
      const { data } = await this.$axios.get('/get_top_players', { grid: this.$store.state.grid })
      this.topAnswersGrid = data
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
