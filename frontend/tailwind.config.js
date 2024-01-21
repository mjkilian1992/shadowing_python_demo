/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
        "../newsletter/templates/**/*.html",
        "../customer/templates/**/*.html",
        "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    fontFamily: {
        'sans-serif': ['Source Sans Pro', 'sans-serif'],
        'serif': ['Libre Baskerville', 'serif'],
    },
  },
  plugins: [
        require('flowbite/plugin')
    ]
}

