<template>
    <div class="main">
        <div class="container">
            <svg class="logo-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zM16 27a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zM16 40a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2zm13 0a2 2 0 0 1-2 2h-6a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2z" fill="#59d185"></path>
            </svg>
            <h2 class="title">INFINITE BASEBALL GRID</h2>
            <div class="social-icons">
                <a href="https://twitter.com/sam_coan">
                    <img src="~/static/twitter.svg" alt="Twitter Logo" />
                </a>
                <a href="https://github.com/slxmmy999/InfiniteImmaculateGrid">
                    <img src="~/static/github.svg" alt="Github Logo" />
                </a>
                <a href="https://discord.gg/rPBuvhqG8p">
                    <img src="~/static/discord.svg" alt="Discord" />
                </a>
                <a href="https://allmylinks.com/sam-coan">
                    <img src="~/static/donate.png" alt="Donation Logo" />
                </a>
                <a class="donatelolz" @click="showDonateMenu = !showDonateMenu">
                    <button>Donate $0.69</button>
                </a>
            </div>
        </div>
        <div v-if="showDonateMenu" class="donate69">
            <button class="venmo" @click="venmo">Venmo</button>
            <button @click="paypal">PayPal</button>
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
            align-items: last baseline !important;
        }

        .social-icons a {
            margin-right: 0% !important;
            margin-bottom: 20% !important;
        }

        .donatelolz {
            width: 50% !important;
        }
    }
    .main {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
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

    .donatelolz {
        margin-right: 5% !important;
        margin-bottom: 20% !important;
    }

    .donatelolz button {
        background-color: #141421;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        margin: 0px;
        margin-top: 0%;
        border-radius: 5px;
        border-width: 0;
    }

    .donatelolz button:hover {
        background-color: #21213b;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        margin: 0px;
        margin-top: 0%;
        border-radius: 5px;
        border-width: 0;
    }

    .donate69 {
        display: flex;
        align-items: flex-end;
        flex-direction: column;
        margin-left: auto;
        width: auto;
        padding: 0.2%;
        margin-top: 0%;
        margin-right: 0.7%;
        background-color: #2b2b46;
    }

    .donate69 button {
        background-color: transparent;
        width: fit-content;
        padding: 0%;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        border-radius: 5px;
        border-width: 0;
    }

    .venmo {
        margin-bottom: 70% !important;
    }

    .donate69 button:hover {
        background-color: #21213b;
        color: white;
        font-family: 'Roboto', sans-serif;
    }
</style>

<script>
export default {
  name: 'top-menu',
  data () {
    return {
      showDonateMenu: false
    }
  },
  methods: {
    venmo () {
      window.open('https://account.venmo.com/payment-link?audience=private&amount=0.69&recipients=Sam-Coan-1&txn=pay', '_blank')
    },
    paypal () {
      window.open('https://www.paypal.com/paypalme/samcoan4/0.69', '_blank')
    }
  }
}
</script>
