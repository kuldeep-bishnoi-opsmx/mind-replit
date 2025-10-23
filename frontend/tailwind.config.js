/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        colors: {
          primary: {
            DEFAULT: "#3B82F6",
            foreground: "#FFFFFF",
          },
          secondary: {
            DEFAULT: "#6B7280",
            foreground: "#FFFFFF",
          },
          accent: {
            DEFAULT: "#F59E0B",
            foreground: "#000000",
          },
        },
      },
    },
    plugins: [],
  }

