<template>
    <div :class="$style.grid">
        <div></div> <!-- Empty grid cell -->
        <div :class="[$style['label-container'], $style['top-label']]">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <div :class="[$style['label-container'], $style['top-label']]">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <div :class="[$style['label-container'], $style['top-label']]">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <div></div> <!-- Empty grid cell -->
        <div :class="$style['label-container']">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <div></div> <!-- Empty grid cell -->
        <div :class="$style['label-container']">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <div>
            <div :class="$style['small-text']">GUESSES</div>
            <div :class="$style['large-text']">9</div>
        </div>
        <div :class="$style['label-container']">
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
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
export default {
  name: 'game-grid'
}
</script>
