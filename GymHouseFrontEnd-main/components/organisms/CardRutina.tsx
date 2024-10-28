import Image from "next/image"
import Link from "next/link"
import { FeedStarIcon, BookmarkIcon } from "@primer/octicons-react"
import {TextSubtitle, TextParagraph, hoverscale, sectionCard} from '../tokens'

import {training_plan} from "@/types/training_plan"
import useAuthStore from '@/validators/useAuthStore';
import { useRouter, usePathname } from 'next/navigation';

type CardProps = {
    trainingPlan: training_plan
}

export function CardRutina({ trainingPlan }: CardProps) {
    const pathname = usePathname();
    const { language } = useAuthStore();
    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/${path}`;
    };
    return (
        <article className="flex flex-col items-center h-max w-64 rounded-[20px] m-[20px] border-slate-400 p-4 bg-[#718698]">
            <Link href={buildLink(`/${trainingPlan.id} `)}>
                <Image
                    className={"rounded-md " + hoverscale}
                    src='/logo_gym.png'
                    alt='Logo Gym'
                    width='250'
                    height='200'
                />
            </Link>
            <p className={` ${TextSubtitle} text-center mt-4`}>{trainingPlan.name}</p>
            <p>{trainingPlan.description}</p>
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