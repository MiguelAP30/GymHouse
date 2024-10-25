import type { Metadata } from "next";
import {TextTitle, TextParagraph} from '../../../../components/tokens'
import { useTranslations } from 'next-intl';

export const metadata: Metadata = {
    title: "Exercises",
    description: "Exercises are for people that want to get fit."
};

export default function exercises() {
    const t = useTranslations("exercises")
    return (
        <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
            <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
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
