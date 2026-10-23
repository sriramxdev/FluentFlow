import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
export default defineConfig({ site: 'https://sriramxdev.github.io/FluentFlow', base: '/FluentFlow', integrations: [tailwind()], output: 'static' });
