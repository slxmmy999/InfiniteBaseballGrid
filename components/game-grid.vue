<template>
    <div>
        <div :class="$style['labels-row']">
            <img src="~/static/braves.png" :class="$style.label" />
            <img src="~/static/braves.png" :class="$style.label" />
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
        <div :class="$style['labels-column']">
            <img src="~/static/braves.png" :class="$style.label" />
            <img src="~/static/braves.png" :class="$style.label" />
            <img src="~/static/braves.png" :class="$style.label" />
        </div>
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
    </div>
</template>

<style module>
    .label {
        width: 10%;
    }
    .grid {
        width: 28%;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px; /* adjust as needed */
        border-radius: 15px;
        margin: auto;
        margin-top: 1%;
        margin-left: 0%;
        overflow: hidden;
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

    .labels-row {
        display: flex;
        width: 28%;
        justify-content: space-around;
        margin: auto;
        margin-bottom: 10px; /* Adjust as needed */
    }

    .labels-column {
        width: 28%;
        display: flex;
        flex-direction: column;
        height: 60vh;
        justify-content:space-around; /* Adjust as needed */
        align-items: flex-end;
        margin-right: 1%; /* Adjust as needed */
        margin-left: 7%;
        float: left;
    }
</style>

<script>
export default {
  name: 'game-grid'
}
</script>
