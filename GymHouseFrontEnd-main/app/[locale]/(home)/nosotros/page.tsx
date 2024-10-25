import type { Metadata } from "next";
import {TextTitle, TextParagraph, centerItem} from '../../../../components/tokens'
import { useTranslations } from 'next-intl';


export const metadata: Metadata = {
    title: "GymHouse",
    description: "Gymahouse is fantastic.",
};

export default function About() {
    const t = useTranslations("about")
    return (
        <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
            <aside className={`${centerItem} w-full bg-[#011627] m-0 p-0`}>
                <h1 className={`${TextTitle}`}>
                    {t("title")}
                </h1>
                <p className={`${TextParagraph}`}>
                    {t("message")}
                </p>
            </aside>
        </main>
    );
}