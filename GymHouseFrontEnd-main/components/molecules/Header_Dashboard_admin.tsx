"use client";
import Link from 'next/link';
import { hoverLink } from '../tokens';
import { useTranslations } from 'next-intl';
import useAuthStore from '@/validators/useAuthStore';
import { useRouter, usePathname } from 'next/navigation';

export const HeaderDashboardAdmin = () => {
    const t = useTranslations("");
    const pathname = usePathname();
    const { language } = useAuthStore();

    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/dashboard/administrador/${path}`;
    };

    return (
        <aside className="w-64 bg-gray-800 text-white shadow-lg p-4">
            <nav className="space-y-4 flex flex-col">
                <p className="text-lg font-semibold">Dashboard</p>
                <Link href={buildLink('calificacionEjercicios')} className={`mr-[20px] ${hoverLink}`}>Calificar Ejercicios</Link>
                <Link href={buildLink('dias')} className={`mr-[20px] ${hoverLink}`}>Dias de la Semana</Link>
                <Link href={buildLink('dificultadEjercicios')} className={`mr-[20px] ${hoverLink}`}>Dificultad de Ejercicios</Link>
                <Link href={buildLink('ejercicios')} className={`mr-[20px] ${hoverLink}`}>Ejercicios</Link>
                <Link href={buildLink('etiquetasRutinas')} className={`mr-[20px] ${hoverLink}`}>Etiquetas de las Rutinas</Link>
                <Link href={buildLink('Gimnasios')} className={`mr-[20px] ${hoverLink}`}>Gimnasios</Link>
                <Link href={buildLink('maquinas')} className={`mr-[20px] ${hoverLink}`}>Maquinas</Link>
                <Link href={buildLink('musculosEspecificos')} className={`mr-[20px] ${hoverLink}`}>Musculos Especificos</Link>
                <Link href={buildLink('roles')} className={`mr-[20px] ${hoverLink}`}>Roles</Link>
            </nav>
        </aside>
    );
};