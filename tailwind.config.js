/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './views/**/*.html', // Adjust this path to match your HTML files
    './controllers/**/*.js', // Include any JS files that use Tailwind classes
  ],
  theme: {
    extend: {
      colors: {
        'retro-green': '#32CD32',
        'retro-orange': '#B22222',
        'retro-blue': '#00FFFF',
        'retro-black': '#18181b',
        'retro-gray': '#E0FFFF',
      },
      fontFamily: {
        retro: ['Courier New', 'monospace'], // Retro terminal font
        retro_title: ['"Press Start 2P"', 'monospace'],
      },
      
    },
  },
  plugins: [],
};