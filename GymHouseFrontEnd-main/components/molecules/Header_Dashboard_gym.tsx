"use client";
import Link from 'next/link';
import { hoverLink } from '../tokens';
import { useTranslations } from 'next-intl';
import useAuthStore from '@/validators/useAuthStore';
import { useRouter, usePathname } from 'next/navigation';

export const HeaderDashboardGym = () => {
    const t = useTranslations("");
    const pathname = usePathname();
    const { language } = useAuthStore();

    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/dashboard/${path}`;
    };

    return (
        <aside className="w-64 bg-gray-800 text-white shadow-lg p-4">
            <nav className="space-y-4 flex flex-col">
                <p className="text-lg font-semibold">Dashboard</p>
                <Link href={buildLink('misUsuarios')} className={`mr-[20px] ${hoverLink}`}>Mis Usuarios</Link>
                <Link href={buildLink('gym')} className={`mr-[20px] ${hoverLink}`}>Mi Gimnasio</Link>
            </nav>
        </aside>
    );
};