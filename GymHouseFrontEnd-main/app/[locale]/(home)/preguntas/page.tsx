import {TextTitle, TextParagraph, centerItem} from '../../../../components/tokens'
import { useTranslations } from 'next-intl';

export default function QuestionsPage() {
  const t = useTranslations("faq")
  return (
    <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
      <aside className={`${centerItem} w-full bg-[#011627] m-0 p-0`}>
          <h1 className={`${TextTitle}`}>
            {t("message")}
          </h1>
          <p className={`${TextParagraph}`}>
            ¿Cómo puedo acceder a la plataforma?
          </p>
      </aside>
    </main>
  )
}
