import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
    site: 'https://alphasoundz.github.io/Obsidian-Vault/',
    integrations: [
        starlight({
            title: "AlphaSound'Z Vault",
            social: {
                youtube: 'https://www.youtube.com/channel/UCHC-7HwviJBDd7AaIP_Ys7A',
                github: 'https://github.com/alphasoundz/obsidian-vault',
            },
            sidebar: [
                {
                    label: 'Guides',
                    items: [
                        // Each item here is one entry in the navigation menu.
                        { label: 'Example Guide', link: '/guides/example/' },
                    ],
                },
                {
                    label: 'Reference',
                    autogenerate: { directory: 'reference' },
                },
            ],
        }),
    ],
});
