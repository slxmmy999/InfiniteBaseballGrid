<template>
  <div v-if="isVisible" class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="box">
        <h2 class="title is-4">Share Grid</h2>
        <p class="subtitle is-6">Use this unique link to share this grid with your friends:</p>
        <div class="field is-grouped">
          <p class="control is-expanded">
            <input class="input" type="text" v-model="shareLink" readonly>
          </p>
          <p class="control">
            <button class="copy-button" @click="copyLink">Copy Link</button>
          </p>
        </div>
        <button class="dismiss-button" @click="closeModal">Dismiss</button>
      </div>
    </div>
  </div>
</template>

<script>
import { EventBus } from '~/event-bus.js'

export default {
  data () {
    return {
      isVisible: false,
      shareLink: 'Loading...'
    }
  },
  methods: {
    async openModal () {
      this.isVisible = true
      if (this.shareLink === 'Loading...') {
        const currentGrid = this.$store.state.grid
        const id = await this.$axios.$post('/set_shared_grid',
          {
            grid: currentGrid
          }
        )
        this.shareLink = `https://infinitebaseballgrid.com/?id=${id.id}`
      }
    },
    closeModal () {
      this.isVisible = false
    },
    copyLink () {
      navigator.clipboard.writeText(this.shareLink)
        .then(() => {
          // You can replace this alert with a better notification system
          alert('Link copied to clipboard!')
        })
        .catch((err) => {
          console.error('Could not copy text: ', err)
        })
    }
  },
  created () {
    EventBus.$on('show-share-popup', () => {
      console.log('showing share popup')
      this.openModal()
    })
  }
}
</script>

<style scoped>
.modal.is-active {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5); /* semi-transparent black */
}

.modal-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.modal-content {
  position: relative;
  width: 80%;
  max-width: 600px;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  background: #202020; /* shadow for depth */
}

.title, .subtitle {
  color: white;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.copy-button {
  background: darkolivegreen;
  color: #fff;
  border-radius: 15px;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.dismiss-button {
  background: darkgray;
  color: black;
  border-radius: 15px;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}

.input {
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 5px;
  width: 95%;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}
</style>
