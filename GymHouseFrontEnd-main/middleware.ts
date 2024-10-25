import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
    locales: ['arb', 'en', 'es'],

    defaultLocale: 'es'
});

export const config = {
    matcher: ['/', '/(arb|en|es)/:path*']
};