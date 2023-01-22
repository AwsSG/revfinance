/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './static/src/**/*.js'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'fluorescent-blue': '#44E5E7',
        'han-purple': '#552CE9',
        'white': '#ffffff',
        'raisen-black': '#272727',
        'space-cadet': '#2B2D42',
        'independence': '#404363',
        'baby-powder': '#FCFFFD',
        'rajah': '#F5A65B'
      },
      fontFamily: {
        'archivo-black': ['Archivo Black', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
