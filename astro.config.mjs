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
                    autogenerate: { directory: 'Mathe' },
                    collapsed: true,
                },
                {
                    label: 'Deutsch',
                    autogenerate: { directory: 'Deutsch' },
                    collapsed: true,
                },
                {
                    label: 'Englisch',
                    autogenerate: { directory: 'Englisch' },
                    collapsed: true,
                },
                {
                    label: 'Daily Notes',
                    autogenerate: { directory: 'Daily Notes' },
                    collapsed: true,
                },
                {
                    label: 'Seminar',
                    autogenerate: { directory: 'Seminar' },
                    collapsed: true,
                },
                {
                    label: 'PGW',
                    autogenerate: { directory: 'PGW' },
                    collapsed: true,
                },
                {
                    label: 'Kunst',
                    autogenerate: { directory: 'Kunst' },
                    collapsed: true,
                },
                {
                    label: 'Physik',
                    autogenerate: { directory: 'Physik' },
                    collapsed: true,
                },
                {
                    label: 'Geographie',
                    autogenerate: { directory: 'Geographie' },
                    collapsed: true,
                },
                {
                    label: 'Philosophie',
                    autogenerate: { directory: 'Philosophie' },
                    collapsed: true,
                },
                {
                    label: 'Informatik',
                    autogenerate: { directory: 'Informatik' },
                    collapsed: true,
                },
                {
                    label: 'Musik',
                    autogenerate: { directory: 'Musik' },
                    collapsed: true,
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
            favicon: '/favicon.png',
        }),
    ],
});
