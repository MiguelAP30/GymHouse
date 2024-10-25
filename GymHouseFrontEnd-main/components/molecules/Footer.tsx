'use client';
import Image from 'next/image';
import Link from 'next/link';
import { MarkGithubIcon } from '@primer/octicons-react';
import { hoverscale, hoverLink } from '../tokens';
import useAuthStore from '@/validators/useAuthStore';
import { useRouter } from 'next/navigation'; // Cambia a 'next/navigation'

export const Footer = () => {
    const { setLanguage } = useAuthStore(); // Usar hooks dentro del componente
    const router = useRouter(); // Usar hooks dentro del componente

    // Define una función para manejar el cambio de idioma
    const setLanguagePage = (language: string) => {
        setLanguage(language);
         // Navega a la misma ruta actual
        console.log(`Idioma cambiado a: ${language}`);
    };

    return (
        <footer className="w-full max-w-full h-[140px] bg-[#17455A] flex justify-between items-center p-4">
            <aside className="flex">
                <ul className="flex flex-col ml-0 mr-4">
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}`} href="https://www.instagram.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_instagram.png'
                            alt="logo instagram" 
                            width={50}
                            height={50}
                        />
                        @GymHouse
                    </Link>
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}`} href="https://www.youtube.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_youtube.png'
                            alt="logo youtube" 
                            width={50}
                            height={50}
                        />
                        GymHouseYT
                    </Link>
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}`} href="https://www.twitter.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_twitter.png'
                            alt="logo twitter" 
                            width={50}
                            height={50}
                        />
                        @GymHouse
                    </Link>
                </ul>
            </aside>
            <section className="flex flex-row mr-5">
                <ul className="flex flex-row space-x-4">
                    {/* Enlace a GitHub */}
                    <Link className={`flex flex-row items-center justify-center ${hoverLink} ${hoverscale}`} href="https://github.com/MiguelAP30">
                        <MarkGithubIcon size={80} />
                    </Link>
                </ul>
            </section>
        </footer>
    );
};
