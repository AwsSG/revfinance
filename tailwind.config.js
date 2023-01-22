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
        'rhythm': '#494C6F',
        'baby-powder': '#FCFFFD',
        'rajah': '#F5A65B'
      },
      fontFamily: {
        'archivo-black': ['Archivo Black', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
      },
      boxShadow: {
        'pot-card': 'rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset'
      }
    },
  },
  plugins: [],
};
