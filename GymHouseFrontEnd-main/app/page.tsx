'use client';
import { Header, Footer } from '@/components'
import { mainText } from '@/components/tokens';

export default function Home() {
  return (
    <>
      <Header />
      <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
        <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
          <h1 className="text-[#A3CEF1] pb-6 text-[70px] font-poppins underline underline-offset-4">
              GymHouse
          </h1>
          <p className={`${mainText}`}>
              Transforma tu rutina de ejercicio con nuestra plataforma de gestión para gimnasios, Gymhouse cuenta con: 
              acceso a rutinas personalizadas, herramientas de seguimiento para alcanzar tus metas fitness y un entorno
              social en el que puedes interactura con los demas usuarios.
          </p>
        </aside>
      </main>
      <Footer />
    </>
  );
}
