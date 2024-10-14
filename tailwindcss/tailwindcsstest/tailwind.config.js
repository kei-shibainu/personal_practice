/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        body: "#030303",
        "selected-text": "#A3A3FF",
        theme: "#5c318c",
        "secondary": "#9191A4",
        badge: "#3F3F51",
        inputBorder: "#565666",
        input: "#2A2A33",
      }
    },
    fontFamily: {
      poppins: ["poppins", "sans-serif"]
    }
  },
  plugins: [],
}

