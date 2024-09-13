/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}', 
  ],
  theme: {
    extend: {
      colors: {
        customgreen: '#10B981',
        'customgreen-dark': '#047857',
      },
    },
  },
  plugins: [],
}

