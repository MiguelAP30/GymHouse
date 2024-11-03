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

export function CardRole({ trainingPlan }: CardProps) {
    const pathname = usePathname();
    const { language } = useAuthStore();
    const buildLink = (path: string) => {
        const pathSegments = pathname.split('/');
        const basePath = pathSegments[1] === language ? pathSegments.slice(2).join('/') : pathSegments.slice(1).join('/');
        return `/${language}/${path}`;
    };
    return (
        <article className="flex flex-col items-center h-max w-64 rounded-[20px] m-[20px] border-slate-400 p-4 bg-[#718698]">
            <section className="w-full flex flex-col items-center bg-[#296ca3] rounded-lg p-4">
                <section className="flex flex-col p-4 bg-[#296ca3] rounded-lg w-full">
                    <form className="w-full flex justify-between mb-4">
                        <div className="flex items-center gap-2">
                            <select name="" id="" className="border rounded p-2">
                                <option value="10">10</option>
                            </select>
                            <p>Entries per page</p>
                        </div>
                        <div>
                            <input placeholder="Search" type="text" className="border rounded p-2" />
                        </div>
                    </form>
                    <table className="w-full border-collapse">
                        <thead>
                            <tr>
                                <th className="border p-2">Name</th>
                                <th className="border p-2">Position</th>
                                <th className="border p-2">Office</th>
                                <th className="border p-2">Age</th>
                                <th className="border p-2">Start date</th>
                                <th className="border p-2">Salary</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td className="border p-2">My Name</td>
                                <td className="border p-2">Admin</td>
                                <td className="border p-2">Off Manizales</td>
                                <td className="border p-2">25</td>
                                <td className="border p-2">Hoy</td>
                                <td className="border p-2">00000001</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </section>
        </article>
    )
}