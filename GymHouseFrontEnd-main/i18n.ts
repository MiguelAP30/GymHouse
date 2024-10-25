import { notFound } from 'next/navigation';
import { getRequestConfig } from 'next-intl/server';
import path from 'path';

export const locales = ['en', 'es','arb','man'] as const;
type LocaleType = (typeof locales)[number];

const messagesMap: Record<LocaleType, () => Promise<{ default: any }>> = {
    es: () => import('./messages/es.json'),
    en: () => import('./messages/en.json'),
    arb: () => import('./messages/arb.json'),
    man: () => import('./messages/man.json')
};


export default getRequestConfig(async ({ requestLocale }) => {
    const locale = (await requestLocale) as LocaleType | undefined;

    if (!locale || !locales.includes(locale)) {
        notFound();
    }

    const messages = (await messagesMap[locale]()).default;

    return {
        messages,
    };
});
