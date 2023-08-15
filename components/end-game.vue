<template>
  <div v-if="gameOver" :class="$style.popup">
    <div :class="$style.container">
      <h1 :class="$style.title">Game Over</h1>
      <button :class="$style['popup-button']" @click="newGame()">Play Again</button>
      <button :class="$style['popup-button']" @click="goToMenu()">Back to Grid</button>
      <h2 :class="$style.text" style="margin-top: 5%;"><u>Top Answers:</u></h2>
      <!-- Top Logos -->
      <div :class="$style.grid">
        <div></div> <!-- Empty grid cell -->
        <div v-if="topLogos.length > 0" :class="[$style['label-container'], $style['top-label']]">
          <img :src="topLogos[0][0]" :class="$style.label" />
        </div>
        <div v-if="topLogos.length > 0" :class="[$style['label-container'], $style['top-label']]">
          <img :src="topLogos[1][0]" :class="$style.label" />
        </div>
        <div v-if="topLogos.length > 0" :class="[$style['label-container'], $style['top-label']]">
          <img :src="topLogos[2][0]" :class="$style.label" />
        </div>
        <div></div>
        <div v-if="leftLogos.length > 0" :class="$style['label-container']">
            <img :src="leftLogos[0][0]" :class="$style.label" />
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[0][0].rarity_score }}%</div>
          <img :src="topAnswersGrid[0][0].picture" :class="$style['player-image']" :alt="topAnswersGrid[0][0].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[0][0].name }}</div>
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
            <div :class="$style.rarityScore">{{ topAnswersGrid[0][1].rarity_score }}%</div>
            <img :src="topAnswersGrid[0][1].picture" :class="$style['player-image']" :alt="topAnswersGrid[0][1].name + ' photo'">
            <div :class="$style.playerName">{{ topAnswersGrid[0][1].name }}</div>
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[0][2].rarity_score }}%</div>
          <img :src="topAnswersGrid[0][2].picture" :class="$style['player-image']" :alt="topAnswersGrid[0][2].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[0][2].name }}</div>
        </div>
        <div></div>
        <div v-if="leftLogos.length > 0" :class="$style['label-container']">
            <img :src="leftLogos[1][0]" :class="$style.label" />
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[1][0].rarity_score }}%</div>
          <img :src="topAnswersGrid[1][0].picture" :class="$style['player-image']" :alt="topAnswersGrid[1][0].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[1][0].name }}</div>
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[1][1].rarity_score }}%</div>
          <img :src="topAnswersGrid[1][1].picture" :class="$style['player-image']" :alt="topAnswersGrid[1][1].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[1][1].name }}</div>
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[1][2].rarity_score }}%</div>
          <img :src="topAnswersGrid[1][2].picture" :class="$style['player-image']" :alt="topAnswersGrid[1][2].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[1][2].name }}</div>
        </div>
        <div></div>
        <div v-if="leftLogos.length > 0" :class="$style['label-container']">
            <img :src="leftLogos[2][0]" :class="$style.label" />
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[2][0].rarity_score }}%</div>
          <img :src="topAnswersGrid[2][0].picture" :class="$style['player-image']" :alt="topAnswersGrid[2][0].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[2][0].name }}</div>
        </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[2][1].rarity_score }}%</div>
          <img :src="topAnswersGrid[2][1].picture" :class="$style['player-image']" :alt="topAnswersGrid[2][1].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[2][1].name }}</div>
      </div>
        <div v-if="topAnswersGrid.length > 0" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ topAnswersGrid[2][2].rarity_score }}%</div>
          <img :src="topAnswersGrid[2][2].picture" :class="$style['player-image']" :alt="topAnswersGrid[2][2].name + ' photo'">
          <div :class="$style.playerName">{{ topAnswersGrid[2][2].name }}</div>
      </div>
      <div></div>
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
  align-items: center;
  width: 900px;
  box-sizing: border-box;
  text-align: center;
  max-height: 80vh;
  overflow-y: auto;
}
.grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 4 columns */
  grid-template-rows: repeat(4, 1fr); /* 4 rows to make it square */
  gap: 2px;
  width: 100%;
  max-width: 75vh; /* Set the maximum width to ensure a square aspect ratio */
  margin: auto;
  overflow: hidden;
}

.label-container,
.imageContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  aspect-ratio: 1/1; /* Maintain square aspect ratio */
  width: 100%;
  height: 100%;
}

.label {
  width: 50%;
  height: 50%;
}

.imageContainer {
  flex-direction: column;
  background-color: #00e600;
}

.label-container {
  display: flex;
  aspect-ratio: 1/1;
  justify-content:center;
  align-items: center;
}

.playerName {
  position: relative; /* Absolute positioning */
  bottom: 0; /* Position it at the bottom */
  color: #fff; /* Choose color according to your preference */
  background: rgba(0,0,0,0.6); /* Add a dark background for the text to be visible */
  width: 100%;
  text-align: center; /* To center the text */
  font-family: 'Roboto', sans-serif;
  font-size: 10px;
}

.top-label {
  padding-bottom: 1%;
}

.rarityScore {
  color: white; /* Choose color according to your preference */
  background: rgba(0,0,0,0.6); /* Add a dark background for the text to be visible */
  width: 25%;
  text-align: center; /* To center the text */
  font-family: 'Roboto', sans-serif;
  font-size: 10px;
  align-self: last baseline;
}

.player-image {
  grid-column: span 1;
  width: 50%;
  object-fit: cover;
  /* Add any additional styles for the player images here */
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
      console.log(data)
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
