/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './views/**/*.html', // Adjust this path to match your HTML files
    './controllers/**/*.js', // Include any JS files that use Tailwind classes
  ],
  theme: {
    extend: {
      fontFamily: {
        retro: ['Courier New', 'monospace'], // Retro terminal font
        retro_title: ['"Press Start 2P"', 'monospace'],
      },
     
    },
  },
  plugins: [],
};