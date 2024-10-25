"use client";
import Image from 'next/image';
import Link from 'next/link';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { hoverscale , hoverLink} from '../tokens';
import { useTranslations } from 'next-intl';

export const HeaderRoutines = () => {
    const t = useTranslations("routines")
    return (
        <header className="flex flex-row items-center justify-center w-full bg-[#011627] m-0 p-4">
                <input 
                    type="text" 
                    placeholder="Buscar" 
                    className="w-[10%] h-[50px] rounded-[20px] m-[20px]"
                />
                <Link href="/rutinasGenerales" className={`mr-[20px] ${hoverLink}`}>{t("general")}</Link>
                <Link href="/rutinasProfesionales" className={`mr-[20px] ${hoverLink}`}>{t("professional")}</Link>
                <Link href="/rutinasUsuarios" className={`mr-[20px] ${hoverLink}`}>{t("user")}</Link>
                <Link href="/rutinasTodas" className={`mr-[20px] ${hoverLink}`}>{t("all")}</Link>
                <Link href="/rutinasMias" className={`mr-[20px] ${hoverLink}`}>{t("mine")}</Link>
        </header>
    )
}