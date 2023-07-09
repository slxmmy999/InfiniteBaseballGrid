<template>
    <div :class="$style.grid">
        <div></div> <!-- Empty grid cell -->
        <img src="~/static/braves.png" :class="$style.label" />
        <img src="~/static/braves.png" :class="$style.label" />
        <img src="~/static/braves.png" :class="$style.label" />
        <img src="~/static/braves.png" :class="$style.label" />
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <img src="~/static/braves.png" :class="$style.label" />
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <img src="~/static/braves.png" :class="$style.label" />
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
    </div>
</template>

<style module>
    .grid {
        display: grid;
        width: 45%;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5px;
        margin: auto;
        overflow: hidden;
    }

    .label {
        grid-column: span 1;
        width: 60%;
        display: flex;
        justify-content: center;
        align-items: center;
        /* Add any additional styles for the labels here */
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
</style>

<script>
export default {
  name: 'game-grid'
}
</script>
