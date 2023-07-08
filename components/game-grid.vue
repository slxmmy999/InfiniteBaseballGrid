<template>
    <div :class="$style.grid">
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
        <button :class="$style['grid-item']"></button>
    </div>
</template>

<style module>
    .grid {
        width: 25%;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px; /* adjust as needed */
        border-radius: 15px;
        margin: auto;
        padding-top: 10%;
    }

    .grid-item {
        aspect-ratio: 1 / 1;
        background-color: #383842; /* adjust as needed */
        color: white; /* adjust as needed */
        border: none; /* adjust as needed */
        padding: 10px; /* adjust as needed */
        font-size: 1em; /* adjust as needed */
        cursor: pointer;
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
