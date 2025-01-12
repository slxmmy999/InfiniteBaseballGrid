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
                <div class="dropdown" @mouseenter="showItem" @mouseleave="delay">
                    <a class="dropbtn" href="#">
                        <img src="~/static/discord.svg" alt="Discord" />
                    </a>
                    <div class="dropdown-content">
                        <a href="https://discord.gg/rPBuvhqG8p">Infinite Baseball Grid Official</a>
                        <a href="https://discord.gg/8yGssB5E9u">Ordinary Effort Official</a>
                    </div>
                </div>
                <a href="https://allmylinks.com/sam-coan">
                    <img src="~/static/donate.png" alt="Donation Logo" />
                </a>
            </div>
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



    .dropdown
    {
        display: flex;
        position: relative;
        margin-right: 40%;
    }
  .dropbtn img {
    width: 32px;
    height: 32px;
    transition: transform 0.3s ease;
  }

  .dropbtn:hover img {
    transform: scale(1.1);
  }

  .dropdown-content {
    visibility: hidden;
    display: block;
    position: absolute;
    background-color: #2c2f33;
    min-width: 200px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    z-index: 1;
    border-radius: 8px;
    overflow: hidden;
 /* Position below the button */
    right: 0; /* Align to the right edge of the button */
    transform: translateX(-20%); /* Jut out to the left */
  }

  .dropdown-content a {
    color: #ffffff;
    padding: 12px 100% 12px 16px;
    width: 95%;
    text-decoration: none;
    display: block;
    font-family: Arial, sans-serif;
    font-size: 14px;
    transition: background-color 0.2s;
  }

  .dropdown-content a:hover {
    background-color: #5865f2;
  }
</style>

<script>
export default {
  name: 'top-menu',
    data() {
        return {
            isHidden: true,
            hideTimeout: null,
        };
    },
    methods: {
        showItem() {
            clearTimeout(this.hideTimeout);
            document.querySelector('.dropdown-content').style.visibility = 'visible';
        },
        delay() {
        this.hideTimeout = setTimeout(() => {
            document.querySelector('.dropdown-content').style.visibility = 'hidden';
        }, 300);
        },
    },
}
</script>
