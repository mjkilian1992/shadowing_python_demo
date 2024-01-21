/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
        "../crm_backed_site/templates/**/*.html",
        "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    fontFamily: {
        'sans-serif': ['Source Sans Pro', 'sans-serif'],
        'serif': ['Libre Baskerville', 'serif'],
    },
    extend: {
        colors: {
            "blue": "#5782bb",
            "blue-light": "#7b9dca",
            "blue-dark": "#40699f",
            "black": "#111111",
            "grey-black": "#2a2a2a",

            "theme-bg": "#ffffff",
            "theme-primary": "#5782bb",
            "theme-secondary": "#7b9dca",
            "theme-text": "#111111",
            "theme-grey": "#2a2a2a",

            "dark-theme-bg": "#7b9dca",
            "dark-theme-primary": "#ffffff",
            "dark-theme-secondary": "#5782bb",
            "dark-theme-text": "#eeeeee",
            "dark-theme-grey": "#2a2a2a",
        }
    },
  },
  plugins: [
        require('flowbite/plugin')
    ]
}

