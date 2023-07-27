const env = "prod"; // dev, prod
let baseURL;

if(env === "dev") {
  baseURL = "http://localhost:5000";
} else if(env === "prod") {
  baseURL = "https://api.infiniteimmaculategrid.com";
}

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Infinite Immaculate Grid',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Practice your Immaculate Grid skills with this community supported open source version! Play as many grids as you\'d like with no daily limit!' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap' }
    ]
  },

  server: {
    host: '0.0.0.0',
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/global.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vercel.js', mode: 'client'},
    { src: '~/plugins/adsense.js', mode: 'client' }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/google-analytics'
  ],

  googleAnalytics: {
    id: 'G-G9XV3ZYH0B'
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: baseURL
  },

  publicRuntimeConfig: {
    axios: {
      browserBaseURL: baseURL
    }
  },

  target: 'static',
  buildDir: 'dist',

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
