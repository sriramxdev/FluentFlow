/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: { extend: { colors: { ink: '#0f172a', slatepanel: '#111827', cyanaccent: '#38bdf8' }, boxShadow: { glow: '0 0 35px rgba(56, 189, 248, 0.12)' } } },
  plugins: []
};
