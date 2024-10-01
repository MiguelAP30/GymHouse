import Image from "next/image"
import Link from "next/link"
import {TextSubtitle, TextParagraph, hoverLink} from '../tokens'

type CardProps = {
    idCard: string
}
export function CardDia({idCard}: CardProps) {
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
            <Link href={`/ejercicios/${idCard} `}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 1</p>
            </Link>
            <Link href={`/ejercicios/${idCard} `}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 2</p>
            </Link>
            <Link href={`/ejercicios/${idCard} `}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 3</p>
            </Link>
            <Link href={`/ejercicios/${idCard} `}>
                <p className={`${TextParagraph} text-center mt-1  ${hoverLink}`}>Ejercicio 4</p>
            </Link>
        </article>
    )
}