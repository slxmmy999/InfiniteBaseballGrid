<template>
  <div v-if="gameOver" :class="$style.popup">
    <div :class="$style.container">
      <h2 :class="$style.title">Game Over</h2>
      <p :class="$style.text">You scored {{ $store.state.score }} points!</p>
      <button :class="$style['popup-button']" @click="newGame()">Play Again</button>
      <button :class="$style['popup-button']" @click="goToMenu()">Main Menu</button>
      <!-- Top Logos -->
      <div v-if="topLogos.length > 0" :class="$style.topLogos">
        <img v-for="(logo, index) in topLogos" :key="index" :src="logo[0]" alt="Team Logo">
      </div>
      <!-- Grid with top player answers for each space -->
      <div v-if="topAnswersGrid.length > 0 && leftLogos.length > 0" :class="$style.grid">
        <div v-for="(answer, idx) in rotatedGrid" :key="idx" :class="$style.cell">
          <img :src="leftLogos[idx % 3][0]" alt="Team Logo">
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
  display: grid; /* Change to grid display */
  grid-template-columns: repeat(3, 1fr); /* Define 3 columns */
  gap: 10px; /* Optional: Add some space between cells */
  padding-top: 10%;
  width: 100%;
  margin: auto;
}

.cell {
  border-radius: 5px;
  aspect-ratio: 1/1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: #fff solid 2px;
  width: 100%; /* Set to 100% to fill the grid cell */
  height: auto; /* Allow height to be determined by aspect ratio */
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

.topLogos {
  display: flex;
  justify-content: center;
}

.cell {
  /* Existing styles */
  flex-direction: row; /* Adjust layout */
}

.cell img {
  /* Style your left logos here */
  width: 50px;
  height: 50px;
  margin-right: 10px; /* Add space between the logo and content */
}

.topLogos img {
  /* Style your top logos here */
  width: 50px;
  height: 50px;
  margin-right: 10px; /* Add space between logos */
}

</style>

<script>
import { EventBus } from '../event-bus.js'

export default {
  data () {
    return {
      gameOver: false,
      topAnswersGrid: [],
      topLogos: [],
      leftLogos: []
    }
  },
  created () {
    EventBus.$on('game-over', async () => {
      this.topLogos = this.$store.state.grid[0]
      this.leftLogos = this.$store.state.grid[1]
      this.gameOver = true
      const { data } = await this.$axios.post('/get_top_players', { grid: this.$store.state.grid })
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
  },
  computed: {
    rotatedGrid () {
      // Assuming flatList is a flat array representing your 3x3 grid
      const flatList = this.topAnswersGrid

      console.log(this.topAnswersGrid)
      console.log(flatList)

      // Reshape the flat list into a 3x3 grid
      const originalGrid = []
      for (let i = 0; i < flatList.length; i += 3) {
        originalGrid.push(flatList.slice(i, i + 3))
      }

      // Transpose the 3x3 grid (switch rows and columns)
      const transposedGrid = originalGrid[0].map((_, colIndex) => originalGrid.map(row => row[colIndex]))

      // If you want to keep the result as a flat list, you can flatten it again
      return transposedGrid.flat()
    }
  }
}
</script>
