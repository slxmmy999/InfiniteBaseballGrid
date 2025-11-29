const path = require('path')
const env = "dev";
export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Infinite Baseball Grid',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Practice your Immaculate Grid skills with this community supported open source version! Play as many grids as you\'d like with no daily limit! This is a seperate community project not associated with Sports Reference or Immaculate Grid.' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/static/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap' }
    ],
    __dangerouslyDisableSanitizers: ['script'],
    script: [
      { src: 'https://www.googletagmanager.com/gtag/js?id=G-G9XV3ZYH0B', async: true },
      {
        innerHTML: `if (top !== self) top.location.replace(self.location.href);`,
        type: 'text/javascript',
        charset: 'utf-8'
      }
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
    { src: '~/plugins/gtm.js', mode: 'client' },
    { src: '~/plugins/directives.js', mode: 'client' },
    { src: '~/plugins/axios-config.js', mode: 'client' },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/google-analytics'
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

  target: 'static',
  buildDir: 'dist',

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, { isDev, isClient }) {
      // Run Babel on vue2-gtm in node_modules
      config.module.rules.push({
        test: /\.js$/,
        loader: 'babel-loader',
        include: [
          path.resolve(__dirname, 'node_modules/@gtm-support/vue2-gtm'),
          path.resolve(__dirname, 'node_modules/@gtm-support/core')
        ],
        options: {
          presets: ['@babel/preset-env']
        }
      })
    }
  }
}
