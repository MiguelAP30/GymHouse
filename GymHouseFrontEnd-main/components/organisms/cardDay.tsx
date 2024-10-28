import Image from "next/image"
import Link from "next/link"
import {TextSubtitle, TextParagraph, hoverLink} from '../tokens'

import useAuthStore from '@/validators/useAuthStore';
import { useRouter, usePathname } from 'next/navigation';

type CardProps = {
    idCard: string
}
export function CardDia({idCard}: CardProps) {
    const pathname = usePathname();
    const { language } = useAuthStore();
    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/${path}`;
    };
    return (
        <article className="flex flex-col items-center h-max rounded-[20px] m-[20px] border-slate-400 p-4 bg-[#505e6a]">
            <p className={`${TextSubtitle}`}>Dia de la Semana</p>
            <Image
                className={"rounded-md "}
                src='/musculos.png'
                alt='Logo Gym'
                width='250'
                height='200'
            />
            <Link href={buildLink(`/ejercicios/${idCard} `)}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 1</p>
            </Link>
            <Link href={buildLink(`/ejercicios/${idCard} `)}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 2</p>
            </Link>
            <Link href={buildLink(`/ejercicios/${idCard} `)}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 3</p>
            </Link>
            <Link href={buildLink(`/ejercicios/${idCard} `)}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 4</p>
            </Link>
        </article>
    )
}