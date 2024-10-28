"use client";
import Link from 'next/link';
import { hoverLink } from '../tokens';
import { useTranslations } from 'next-intl';
import useAuthStore from '@/validators/useAuthStore';
import { useRouter, usePathname } from 'next/navigation';

export const HeaderRoutines = () => {
    const t = useTranslations("routines");
    const pathname = usePathname();
    const { language } = useAuthStore();

    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/${path}`;
    };

    return (
        <header className="flex flex-row items-center justify-center w-full bg-[#011627] m-0 p-4">
            <input 
                type="text" 
                placeholder="Buscar" 
                className="w-[10%] h-[50px] rounded-[20px] m-[20px]"
            />
            <Link href={buildLink('rutinasGenerales')} className={`mr-[20px] ${hoverLink}`}>{t("general")}</Link>
            <Link href={buildLink('rutinasProfesionales')} className={`mr-[20px] ${hoverLink}`}>{t("professional")}</Link>
            <Link href={buildLink('rutinasUsuarios')} className={`mr-[20px] ${hoverLink}`}>{t("user")}</Link>
            <Link href={buildLink('rutinasTodas')} className={`mr-[20px] ${hoverLink}`}>{t("all")}</Link>
            <Link href={buildLink('rutinasMias')} className={`mr-[20px] ${hoverLink}`}>{t("mine")}</Link>
        </header>
    );
};