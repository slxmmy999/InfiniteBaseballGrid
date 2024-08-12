<template>
    <div v-if="showModeSelect" :class="$style.container">
        <div :class="$style.modeSelectContainer">
            <div :class="$style.radioContainer">
                <input type="radio" id="option1" name="mode" value="option1"  v-model="selectedMode" :class="$style.radioButton">
                <label for="option1" :class="$style.label">Players only</label>
            </div>
            <div :class="$style.radioContainer">
                <input type="radio" id="option2" name="mode" value="option2" v-model="selectedMode" :class="$style.radioButton" disabled>
                <label for="option2" :class="$style.label">Stats + Players (Coming Soon!)</label>
            </div>
            <div :class="$style.radioContainer">
                <input type="radio" id="option3" name="mode" value="option3" v-model="selectedMode" :class="$style.radioButton" disabled>
                <label for="option3" :class="$style.label">Stats only (Coming Soon!)</label>
            </div>
            <button @click="setMode" :class="$style.closeButton">Close</button>
        </div>
    </div>
</template>

<script>
    import { EventBus } from '../event-bus.js';
    export default {
        name: 'ModeSelect',
        data () {
            return {
                selectedMode: 'option1',
                showModeSelect: false,
                mode: 'players-only',
            };
        },
        methods: {
            setMode () {
                if (this.showModeSelect) {
                    this.showModeSelect = false
                } else {
                    this.showModeSelect = true
                }
                this.$store.commit('gameMode', this.modeode)
            },
        },
        mounted () {
            EventBus.$on('show-mode-select', () => {
                this.showModeSelect = true
            })
        }
    };
</script>

<style module scoped>
.container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.modeSelectContainer {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.radioContainer {
    margin-bottom: 10px;
}

.radioButton {
    margin-right: 10px;
}

.label {
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
    font-size: 16px;
    color: #333;
}

.closeButton {
    align-self: flex-end;
    padding: 10px 20px;
    background-color: #00e600;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-weight: 700;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

:disabled {
    cursor: not-allowed;
    opacity: 0.5;
}

.closeButton:hover {
    background-color: #00cc00;
}
</style>
