<template>
    <div class="search-wrapper" v-if="showSearch">
      <div id="headlessui-dialog-panel" class="search-dialog relative mx-auto max-w-xl transform divide-y divide-gray-100 dark:divide-gray-800 overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black ring-opacity-5 transition-all">
          <div class="relative" v-on-clickaway="hideSearch">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" class="search-icon pointer-events-none absolute left-4 top-3.5 h-5 w-5 text-gray-400">
                  <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clip-rule="evenodd"></path>
              </svg>
              <input v-model="searchTerm"
              @input="onInput"
              aria-expanded="false"
              aria-autocomplete="list"
              id="headlessui-combobox-input"
              role="combobox"
              type="text"
              tabindex="0"
              class="h-12 w-full border-0 bg-transparent dark:bg-gray-700 pl-11 pr-9 text-gray-900 dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-200 focus:ring-0 sm:text-sm"
              placeholder="Search...">
          </div>
          <div v-show="showDropdown" v-on-clickaway="closeDropdown" class="dropdown absolute z-20 mt-1 w-full bg-white rounded-md shadow-lg">
              <div v-for="item in searchResults" :key="item" class="px-4 py-2 hover:bg-gray-200 cursor-pointer" @click="playerClicked(item)">
                  {{ item }}
              </div>
          </div>
      </div>
    </div>
</template>

<script>
import { mixin as clickaway } from 'vue-clickaway'
import { EventBus } from '~/event-bus.js'

export default {
  name: 'game-grid',
  mixins: [clickaway],
  data () {
    return {
      searchTerm: '',
      showDropdown: false,
      searchResults: [],
      showSearch: false
    }
  },
  created () {
    EventBus.$on('show-search', () => {
      this.showSearch = true
    })
  },
  methods: {
    async onInput () {
      const data = await this.$axios.get('/search_players?name=' + this.searchTerm)
      this.searchResults = data.data.filter(item => item.toLowerCase().includes(this.searchTerm.toLowerCase()))
      this.showDropdown = true
    },
    closeDropdown () {
      this.showDropdown = false
    },
    hideSearch () {
      this.showSearch = false
      this.searchTerm = ''
      this.$store.commit('clearAllOnExit')
    },
    playerClicked (player) {
      this.$store.commit('setSelectedPlayer', player.split('|')[0].trim())
      EventBus.$emit('player-selected')
    }
  }
}
</script>

<style scoped>
@media screen and (max-width: 768px) {
  .search-dialog {
    width: 90% !important;
  }

  .search-dialog input {
    font-size: 14px !important;
    width: 95% !important;
  }
}

.search-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
}

.search-dialog {
  width: 60%;
  padding: 20px;
  background: #fff;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
  border-radius: 10px;
}

.search-icon {
  height: 20px;
  width: 20px;
  fill: #888;
}

.search-dialog input {
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  width: 100%;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.1);
}

.search-dialog .dropdown {
  margin-top: 10px;
  border-radius: 6px;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.1);
  overflow: hidden; /* To follow the border-radius for children */
}

.search-dialog .dropdown div {
  padding: 10px;
  cursor: pointer;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.search-dialog .dropdown div:hover {
  background-color: #f6f6f6; /* Light hover effect */
}
</style>
