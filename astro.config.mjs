import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
    site: 'https://notes.alphasoundz.app',
    integrations: [
        starlight({
            title: 'AlphaSoundZ',
            social: {
                youtube: 'https://www.youtube.com/channel/UCHC-7HwviJBDd7AaIP_Ys7A',
                github: 'https://github.com/alphasoundz',
                discord: 'https://discord.gg/QmFnRjNutw',
                instagram: 'https://www.instagram.com/alphasoundzonyt/',
            },
            sidebar: [
                {
                    label: 'Mathe',
                    autogenerate: { directory: 'mathe' },
                },
            ],
            customCss: process.env.NO_GRADIENTS ? [] : ['./src/assets/landing.css'],
            logo: {
                src: './src/assets/logo.png',
            },
            editLink: {
                baseUrl: 'https://github.com/AlphaSoundZ/Obsidian-Vault/edit/app/',
            },
            lastUpdated: true,
            pagination: false,
            favicon: './src/assets/logo.png',
        }),
    ],
});
