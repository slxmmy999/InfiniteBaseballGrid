import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const createStore = () => {
  return new Vuex.Store({
    state: {
      selectedGridLocation: null,
      selectedPlayer: null,
      grid: null,
      gameMode: 'players_only'
    },
    mutations: {
      setSelectedGridLocation (state, item) {
        state.selectedGridLocation = item
      },
      setSelectedPlayer (state, item) {
        state.selectedPlayer = item
      },
      clearAllOnExit (state) {
        state.selectedGridLocation = null
        state.selectedPlayer = null
      },
      setGrid (state, item) {
        state.grid = item
      },
      setGameMode (state, item) {
        state.gameMode = item
      }
    }
  })
}

export default createStore
