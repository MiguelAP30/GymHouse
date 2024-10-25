import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
    locales: ['arb', 'en', 'es'],
    defaultLocale: 'es'
});

export const config = {
    matcher: [
        '/:locale(arb|en|es)/:path*',
        '/'
    ]
};