<template>
    <div :class="$style.grid">
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
            <img :src="teams[0][0][0]" :class="$style.label" />
        </div>
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
            <img :src="teams[0][1][0]" :class="$style.label" />
        </div>
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
            <img :src="teams[0][2][0]" :class="$style.label" />
        </div>
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][0][0]" :class="$style.label" />
        </div>
        <div v-if="gridStatus['s00'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s00'].picture" :class="$style['player-image']" :alt="gridStatus['s00'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s00'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s00')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s01'] != false" :class="$style.imageContainer">
            <img :src="gridStatus['s01'].picture" :class="$style['player-image']" :alt="gridStatus['s01'].name + ' photo'">
            <div :class="$style.playerName">{{ gridStatus['s01'].name }}</div>
        </div>
        <button v-else @click="buttonClicked('s01')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s02'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s02'].picture" :class="$style['player-image']" :alt="gridStatus['s02'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s02'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s02')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][1][0]" :class="$style.label" />
        </div>
        <div v-if="gridStatus['s10'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s10'].picture" :class="$style['player-image']" :alt="gridStatus['s10'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s10'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s10')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s11'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s11'].picture" :class="$style['player-image']" :alt="gridStatus['s11'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s11'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s11')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s12'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s12'].picture" :class="$style['player-image']" :alt="gridStatus['s12'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s12'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s12')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div>
            <div :class="$style['small-text']">GUESSES</div>
            <div :class="$style['large-text']">{{ guesses }}</div>
        </div>
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][2][0]" :class="$style.label" />
        </div>
        <div v-if="gridStatus['s20'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s20'].picture" :class="$style['player-image']" :alt="gridStatus['s20'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s20'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s20')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s21'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s21'].picture" :class="$style['player-image']" :alt="gridStatus['s21'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s21'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s21')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s22'] != false" :class="$style.imageContainer">
          <img :src="gridStatus['s22'].picture" :class="$style['player-image']" :alt="gridStatus['s22'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s22'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s22')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <button v-if="gameOver" :class="$style.newgame" @click="newGame()">New Grid</button>
        <div v-else></div> <!-- Empty grid cell -->
    </div>
</template>

<style module>
    @media screen and (max-width: 768px) {
        .grid {
            width: 100% !important;
            margin-top: 20% !important;
        }

        .large-text {
            font-size: 30px !important;
        }

        .small-text {
            font-size: 10px !important;
        }

        .playerName {
            font-size: 8px !important;
        }

        .newgame {
            font-size: 10px !important;
            height: 100% !important;
        }
    }

    .grid {
        display: grid;
        width: 55%;
        grid-template-columns: repeat(5, 1fr);
        gap: 2px;
        margin: auto;
        overflow: hidden;
    }

    .newgame {
        grid-column: 5 5;
        width: 100%;
        height: 50%;
        border-radius: 15px;
        background-color: red;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        font-size: 20px;
        border: none;
        cursor: pointer;
    }

    .newgame:hover {
        background-color: #ff1a1a;
    }

    .label {
        grid-column: span 1;
        width: 60%;
        height: 65%;
        /* Add any additional styles for the labels here */
    }

    .imageContainer {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      background-color: #00e600;
    }

    .label-container {
        display: flex;
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
      font-size: 14px;
  }

    .top-label {
        padding-bottom: 7%;
    }

    .player-image {
        grid-column: span 1;
        width: 55%;
        object-fit: cover;
        /* Add any additional styles for the player images here */
    }

    .grid-item {
        aspect-ratio: 1 / 1;
        padding: 10%;
        border: none;
        background-color: #383842;
        /* Other styles... */
    }

    .grid-item:hover {
        background-color: #565666; /* adjust as needed */
    }

    .large-text {
        font-size: 350%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }

    .small-text {
        padding-top: 25%;
        font-size: 70%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }
</style>

<script>
import { EventBus } from '~/event-bus.js'

export default {
  name: 'game-grid',
  data () {
    return {
      teams: [],
      guesses: 9,
      gameOver: false,
      gridStatus: {
        s00: false,
        s01: false,
        s02: false,
        s10: false,
        s11: false,
        s12: false,
        s20: false,
        s21: false,
        s22: false
      }
    }
  },
  methods: {
    async buttonClicked (buttonID) {
      console.log('Button clicked. Emitting event...')
      await this.$store.commit('setSelectedGridLocation', buttonID)
      EventBus.$emit('show-search')
    },
    newGame () {
      parent.location.reload()
    }
  },
  async created () {
    const { data } = await this.$axios.get('/get_new_grid')
    this.teams = data
    EventBus.$on('player-selected', async () => {
      const player = this.$store.state.selectedPlayer
      for (const keys in this.gridStatus) {
        if (this.gridStatus[keys] !== false) {
          if (this.gridStatus[keys].name === player) {
            return alert('Player already selected! Please choose another.')
          }
        }
      }
      this.guesses--
      let team1 = ''
      let team2 = ''
      let location = ''
      console.log(this.$store.state.selectedGridLocation)
      switch (this.$store.state.selectedGridLocation) {
        case 's00':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][0][1]
          location = 's00'
          break
        case 's01':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][0][1]
          location = 's01'
          break
        case 's02':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][0][1]
          location = 's02'
          break
        case 's10':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][1][1]
          location = 's10'
          break
        case 's11':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][1][1]
          location = 's11'
          break
        case 's12':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][1][1]
          location = 's12'
          break
        case 's20':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][2][1]
          location = 's20'
          break
        case 's21':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][2][1]
          location = 's21'
          break
        case 's22':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][2][1]
          location = 's22'
          break
      }
      const data = await this.$axios.get(`/validate_player?name=${player}&team1=${team1}&team2=${team2}`)
      if (Object.keys(data.data).length > 0) {
        this.gridStatus[location] = data.data
      }
      this.$store.commit('clearAllOnExit')
      if (this.guesses === 0) {
        this.gameOver = true
      }
    })
  }
}
</script>
