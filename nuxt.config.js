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

  // The head section specifies global page headers that will be included in the HTML <head> section of all pages. 
  //It defines the title of the website, sets the language attribute to English (en), and includes meta tags and link tags for various purposes, 
  //such as defining the character set, viewport settings, and CSS stylesheets.
  
  server: {
    host: '0.0.0.0',
  },

  env: {
    baseUrl: '' // Replace with your Flask API URL
  },

  //The server section configures the Nuxt.js development server. 
  //Setting host to '0.0.0.0' means the server will listen on all available network interfaces, allowing access from any IP address.

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/global.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vercel.js', mode: 'client'}
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  //The css array specifies a global CSS file (global.css) that will be applied to all pages in the application. 
  //The plugins array includes a client-side plugin (vercel.js) that will be executed on the client (browser) side.

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/'
  },

  //The buildModules section includes a single module, @nuxtjs/eslint-module, which enables ESLint for linting the code during development.
  //The modules section includes several modules that extend the functionality of the Nuxt.js application. 
  //These modules include @nuxtjs/axios, which provides an easy way to make HTTP requests, and @nuxtjs/google-analytics, 
  //which integrates Google Analytics into the application.
  //The googleAnalytics object provides the Google Analytics tracking ID to be used for the application.
  //The axios object configures the Axios module, setting the baseURL to the previously defined baseURL.
  //The publicRuntimeConfig object is used for exposing runtime configuration variables to the client-side (browser). 
  //In this case, it exposes the baseURL as browserBaseURL, making it available in client-side code.

  target: 'static',
  buildDir: 'dist',

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}

//The target is set to 'static', indicating that the application will be generated as a static site. 
//Static sites do not require a server-side runtime and can be served as static files.
//The buildDir specifies the directory where the generated files will be stored.
//The build section can include additional build configuration options, but in this code snippet, it is left empty.

//Overall, this code is a Nuxt.js configuration file that sets up various aspects of the application, 
//including server settings, global styles, plugins, modules, and build options. 
//The code also differentiates between development and production environments by dynamically setting the baseURL 
//for Axios requests based on the value of the env variable.
