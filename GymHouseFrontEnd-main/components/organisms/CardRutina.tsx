import Image from "next/image"
import Link from "next/link"
import { FeedStarIcon, BookmarkIcon } from "@primer/octicons-react"
import {TextSubtitle, TextParagraph, hoverscale, sectionCard} from '../tokens'

type CardProps = {
    idCard: string
}
export function CardRutina({idCard}: CardProps) {
    return (
        <article className="flex flex-col items-center h-max rounded-[20px] m-[20px] border-slate-400 p-4 bg-[#718698]">
            <Link href={`/${idCard} `}>
                <Image
                    className={"rounded-md " + hoverscale}
                    src='/logo_gym.png'
                    alt='Logo Gym'
                    width='250'
                    height='200'
                />
            </Link>
            <p className={` ${TextSubtitle} text-center mt-4`}>Nombre De La Rutina</p>
            <p>El id de la rutina es {idCard}</p>
            <section className={`${sectionCard}`}>
                <p className={`${TextParagraph} text-center mt-2`}>10</p>
                <FeedStarIcon size={20} className="ml-2 mt-[8px]" />
            </section>
            <section className={`${sectionCard} mt-1`}>
                <button className={"p-2 bg-slate-700 rounded mt-4"+ hoverscale }>
                    Add to cart
                </button>
                <button className="mt-[5px]">
                    <BookmarkIcon size={30} className={hoverscale}/>
                </button>
            </section>
        </article>
    )
}