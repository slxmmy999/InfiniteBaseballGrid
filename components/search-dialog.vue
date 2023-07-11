<template>
    <div id="headlessui-dialog-panel" class="relative mx-auto max-w-xl transform divide-y divide-gray-100 dark:divide-gray-800 overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black ring-opacity-5 transition-all">
        <div class="relative">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" class="pointer-events-none absolute left-4 top-3.5 h-5 w-5 text-gray-400">
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
        <div v-show="showDropdown" v-on-clickaway="closeDropdown" class="absolute z-20 mt-1 w-full bg-white rounded-md shadow-lg">
            <div v-for="item in searchResults" :key="item" class="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                {{ item }}
            </div>
        </div>
    </div>
</template>

<script>
import { mixin as clickaway } from 'vue-clickaway'

export default {
  mixins: [clickaway],
  data () {
    return {
      searchTerm: '',
      showDropdown: false,
      searchResults: []
    }
  },
  methods: {
    onInput () {
      // Simulate API call
      this.searchResults = ['Result 1', 'Result 2', 'Result 3', 'Result 4', 'Result 5'].filter(item => item.toLowerCase().includes(this.searchTerm.toLowerCase()))
      this.showDropdown = true
    },
    closeDropdown () {
      this.showDropdown = false
    }
  }
}
</script>

<style>
/* Add your styles here */
</style>
