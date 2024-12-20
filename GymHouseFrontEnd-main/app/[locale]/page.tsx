'use client';
import { Header, Footer } from '../../components'
import { mainText } from '../../components/tokens';
import { useTranslations } from 'next-intl';
export default function Home() {
  const t = useTranslations("home")
  return (
    <div className="h-screen flex flex-col">
      <Header />
      <div className="flex-grow">
        <main className="w-full flex justify-between min-h-full m-0 p-0">
          <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
            <h1 className="text-[#A3CEF1] pb-6 text-[70px] font-poppins underline underline-offset-4">
                GymHouse
            </h1>
            <p className={`${mainText}`}>
                {t("message")}
            </p>
          </aside>
        </main>
      </div>
      <Footer />
    </div>
  );
}
