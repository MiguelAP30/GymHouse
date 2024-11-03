import {TextTitle, TextParagraph, centerItem} from '../../../../components/tokens'
import { useTranslations } from 'next-intl';

export default function QuestionsPage() {
  const t = useTranslations("faq")
  return (
    <main className="w-full flex justify-between min-h-full m-0 p-0">
            <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
                <h1 className={`${TextTitle}`}>
                    {t("title")}
                </h1>
                <p className={`${TextParagraph}`}>
                    {t("message")}
                </p>
            </aside>
        </main>
  )
}
