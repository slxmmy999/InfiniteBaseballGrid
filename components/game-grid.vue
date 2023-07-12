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
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '00'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('00')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '01'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('01')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '02'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('02')" :class="$style['grid-item']"></button>
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][1][0]" :class="$style.label" />
        </div>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '10'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('10')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '11'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('11')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '12'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('12')" :class="$style['grid-item']"></button>
        <div>
            <div :class="$style['small-text']">GUESSES</div>
            <div :class="$style['large-text']">9</div>
        </div>
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][2][0]" :class="$style.label" />
        </div>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '20'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('20')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '21'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('21')" :class="$style['grid-item']"></button>
        <div v-if="Object.keys(currPlayerData).length > 0 && currGridPos == '22'">
            <img :src="currPlayerData.picture" alt="">
            <div>{{ currPlayerData.name }}</div>
        </div>
        <button v-else @click="buttonClicked('22')" :class="$style['grid-item']"></button>
        <div></div> <!-- Empty grid cell -->
    </div>
</template>

<style module>
    .grid {
        display: grid;
        width: 45%;
        grid-template-columns: repeat(5, 1fr);
        gap: 2px;
        margin: auto;
        overflow: hidden;
    }

    .label {
        grid-column: span 1;
        width: 60%;
        /* Add any additional styles for the labels here */
    }

    .label-container {
        display: flex;
        justify-content:center;
        align-items: center;
    }

    .top-label {
        padding-bottom: 7%;
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
        font-size: 55px; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }

    .small-text {
        padding-top: 25%;
        font-size: 10px; /* Adjust to your preference */
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
      currPlayerData: {},
      currGridPos: ''
    }
  },
  methods: {
    buttonClicked (buttonID) {
      console.log('Button clicked. Emitting event...')
      this.$store.commit('setSelectedGridLocation', buttonID)
      EventBus.$emit('show-search')
    }
  },
  async created () {
    const { data } = await this.$axios.get('http://127.0.0.1:5000/get_new_grid')
    console.log(data)
    this.teams = data
    EventBus.$on('player-selected', async () => {
      let team1 = ''
      let team2 = ''
      switch (this.$store.state.selectedGridLocation) {
        case '00':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][0][1]
          break
        case '01':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][1][1]
          break
        case '02':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][2][1]
          break
        case '10':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][0][1]
          break
        case '11':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][1][1]
          break
        case '12':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][2][1]
          break
        case '20':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][0][1]
          break
        case '21':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][1][1]
          break
        case '22':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][2][1]
          break
      }
      const data = await this.$axios.get(`http://localhost:5000/validate_player?name=${this.$store.state.selectedPlayer}&team1=${team1}&team2=${team2}`)
      this.currPlayerData = data.data
      this.currGridPos = this.$store.state.selectedGridLocation
    })
  }
}
</script>
