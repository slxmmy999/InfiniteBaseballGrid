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
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][1][0]" :class="$style.label" />
        </div>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <div>
            <div :class="$style['small-text']">GUESSES</div>
            <div :class="$style['large-text']">9</div>
        </div>
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <img :src="teams[1][2][0]" :class="$style.label" />
        </div>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
        <button @click="buttonClicked" :class="$style['grid-item']"></button>
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
      teams: []
    }
  },
  methods: {
    buttonClicked () {
      console.log('Button clicked. Emitting event...')
      EventBus.$emit('show-search')
    }
  },
  async created () {
    const { data } = await this.$axios.get('http://127.0.0.1:5000/get_new_grid')
    console.log(data)
    this.teams = data
  }
}
</script>
