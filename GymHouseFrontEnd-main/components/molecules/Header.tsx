"use client";
import Image from 'next/image';
import Link from 'next/link';
import { useEffect } from 'react';
import { useRouter, usePathname, useSearchParams } from 'next/navigation';
import { hoverscale, hoverLink } from '../tokens';
import useAuthStore from '@/validators/useAuthStore';
import { useTranslations } from 'next-intl';
import {role} from '@/types/roles';

export const Header = () => {
  const { language, isAuthenticated, setIsAuthenticated, fetchToken, nameUser, setToken, setLanguage, rol } = useAuthStore();
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const t = useTranslations("header");

  useEffect(() => {
    const fetchUser = async () => {
      const storedToken = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
      if (storedToken) {
        setToken(storedToken);
        try {
          await fetchToken();
        } catch (error) {
          console.error("Error fetching user token:", error);
          setIsAuthenticated(false);
        }
      } else {
        setIsAuthenticated(false);
      }
    };

    fetchUser();
  }, [setIsAuthenticated, fetchToken, setToken]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('auth');
    setToken(null);
    setIsAuthenticated(false);
    router.push('/');
  };

  // Nueva función para cambiar idioma
  const changeLanguage = (newLanguage: string) => {
    setLanguage(newLanguage); // Cambia el idioma en el estado
    const pathSegments = pathname.split('/');
    const newPath = `/${newLanguage}/${pathSegments.slice(2).join('/')}`; // Cambia el idioma en la ruta
    router.push(newPath); // Navega a la nueva ruta
  };

  return (
    <header className="w-full max-w-full min-h-[70px] shadow-md bg-[#17455A] flex justify-between items-center">
      <aside className="flex justify-center items-center mx-[40px]">
        <Link href="/" className="group">
          <Image
            className={`w-[60px] h-[50px] mr-[10px] ${hoverscale}`}
            src='/logo_gym.png'
            alt="logo del gimnasio"
            width={50}
            height={50}
          />
        </Link>
        <Link href={`/${language}/`} className={`mr-[20px] ${hoverLink}`}>GymHouse</Link>
        <Link href={`/${language}/preguntas`} className={`mr-[20px] ${hoverLink}`}>{t("faq")}</Link>
        <Link href={`/${language}/nosotros`} className={`mr-[20px] ${hoverLink}`}>{t("about")}</Link>
      </aside>
      <div className="flex-grow text-center">
        {isAuthenticated && <h2 className="text-white">¡{t("message")} {nameUser}!</h2>}
      </div>
      <nav className="flex items-center mr-5">
        {isAuthenticated ? (
          <>
            <Link href={`/${language}/rutinasGenerales`} className={`mr-[10px] ${hoverLink}`}>{t("routines")}</Link>
            <Link href={`/${language}/ejercicios`} className={`mr-[10px] ${hoverLink}`}>{t("exercises")}</Link>
            <Link href={`/${language}/perfil`} className={`mr-[10px] ${hoverLink}`}>{t("profile")}</Link>
            {rol !== null && rol == role.admin && <Link href={`/${language}/dashboard/administrador`} className={`mr-[10px] ${hoverLink}`}>Admin Dashboard</Link>}
            {rol !== null && rol == role.gym && <Link href={`/${language}/dashboard/gym`} className={`mr-[10px] ${hoverLink}`}>Gym Dashboard</Link>}
            <input
              type="button"
              value={t("logout")}
              onClick={handleLogout}
              className={`ml-[40px] mr-[10px] ${hoverLink}`}
            />
          </>
        ) : (
          <>
            <Link href={`/${language}/login`} className={`mr-[10px] ${hoverLink}`}>{t("login")}</Link>
            <Link href={`/${language}/register`} className={`mr-[10px] ${hoverLink}`}>{t("register")}</Link>
          </>
        )}
        <ul className="flex space-x-4 ml-5">
          {/* Agrega las banderas como emojis */}
          <li onClick={() => changeLanguage('es')} className={`${hoverLink} ${hoverscale}`}>
            es {/* Bandera de España */}
          </li>
          <li onClick={() => changeLanguage('en')} className={`${hoverLink} ${hoverscale}`}>
          en {/* Bandera del Reino Unido */}
          </li>
          <li onClick={() => changeLanguage('arb')} className={`${hoverLink} ${hoverscale}`}>
            arb {/* Bandera de Arabia Saudita */}
          </li>
          <li onClick={() => changeLanguage('man')} className={`${hoverLink} ${hoverscale}`}>
            man {/* Bandera de China */}
          </li>
        </ul>
      </nav>
    </header>
  );
};
