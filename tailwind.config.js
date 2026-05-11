/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./app/**/*.{js,jsx,ts,tsx}",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#6366F1',
          50: '#EBEEFF',
          100: '#E0E1FF',
          200: '#C7C9FF',
          300: '#A5A7FF',
          400: '#8386FF',
          500: '#6366F1',
          600: '#4F52D9',
          700: '#3D40B8',
          800: '#2E3196',
          900: '#22247A',
        },
        secondary: {
          DEFAULT: '#EC4899',
          50: '#FDF2F8',
          100: '#FCE7F3',
          200: '#FBCFE8',
          300: '#F9A8D4',
          400: '#F472B6',
          500: '#EC4899',
          600: '#DB2777',
          700: '#BE185D',
          800: '#9D174D',
          900: '#831843',
        },
      },
    },
  },
  plugins: [],
};
