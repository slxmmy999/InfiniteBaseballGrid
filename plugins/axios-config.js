export default function ({ $axios }) {
    if (process.client) {
        if (window.location.hostname === 'localhost') {
            const baseURL = `http://localhost:5000/`;
            $axios.defaults.baseURL = baseURL;
        } else {
            const baseURL = `https://api.${window.location.hostname}/`;
            $axios.defaults.baseURL = baseURL;
        }
    }
}