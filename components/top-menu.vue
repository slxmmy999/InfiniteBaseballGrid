<template>
    <div class="container">
        <svg class="logo-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zM16 27a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zM16 40a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2z" fill="#59d185"></path>
        </svg>
        <h2 class="title">INFINITE IMMACULATE GRID</h2>
        <div class="social-icons">
            <a href="https://twitter.com/sam_coan">
                <img src="~/static/twitter.svg" alt="Twitter Logo" />
            </a>
            <a href="https://github.com/slxmmy999/InfiniteImmaculateGrid">
                <img src="~/static/github.svg" alt="Github Logo" />
            </a>
            <a href="https://allmylinks.com/sam-coan">
                <img src="~/static/donate.png" alt="Donation Logo" />
            </a>
        </div>
    </div>
</template>

<style scoped>

    @media screen and (max-width: 768px) {
        .title {
            font-size: 1rem !important;
            width: 50% !important;
            text-align: center !important;
        }

        .social-icons {
            flex-direction: column !important;
        }

        .social-icons a {
            margin-right: 0% !important;
            margin-bottom: 20% !important;
        }
    }
    .logo-svg {
        width: 100px; /* Adjust to your preference */
        height: 100px; /* Adjust to your preference */
        padding-left: 1%;
    }

    .container {
        display: flex;
        width: 100%;
    }

    .title {
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        color: white;
        margin: 0px;
        margin-top: 0.7%;
    }

    .social-icons {
        display: flex;
        align-items: top;
        justify-content: flex-end;
        margin-left: auto;
        margin-top: 0.7%;
    }

    .social-icons a {
        margin-right: 40%; /* Add space between icons */
    }

    .social-icons img {
        width: 30px; /* Adjust to your preference */
        height: 30px; /* Adjust to your preference */
    }
</style>

<script>
export default {
  name: 'top-menu'
}
</script>
