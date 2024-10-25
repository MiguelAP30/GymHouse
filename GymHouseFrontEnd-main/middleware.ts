import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
    locales: ['arb', 'en', 'es'],
    defaultLocale: 'es'
});

export const config = {
    matcher: [
        '/:nextData(_next/data/[^/]{1,})?/(arb|en|es)(/:path*)?',
        '/'
    ]
};