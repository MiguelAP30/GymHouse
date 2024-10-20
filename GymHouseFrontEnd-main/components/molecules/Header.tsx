"use client";
import Image from 'next/image';
import Link from 'next/link';
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { hoverscale, hoverLink } from '../tokens';
import useAuthStore from '@/validators/useAuthStore';

export const Header = () => {
  const { token, isAuthenticated, setIsAuthenticated, fetchToken, rol, nameUser, setToken } = useAuthStore();
  const router = useRouter();

  useEffect(() => {
    const fetchUser = async () => {
      const storedToken = typeof window !== 'undefined' ? localStorage.getItem('token') : null; // Asegúrate de que esto se ejecute solo en el cliente
      if (storedToken) {
        setToken(storedToken); // Establece el token en el store
        await fetchToken(); // Obtén los datos del usuario
      } else {
        setIsAuthenticated(false);
      }
    };

    fetchUser(); // Llama a la función asíncrona dentro de useEffect
  }, [setIsAuthenticated, fetchToken, setToken]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken(null); // Limpia el token en el store
    setIsAuthenticated(false); // Cambia el estado de autenticación
    router.push('/'); // Redirecciona al logout
  };

  return (
    <header className="w-full max-w-full h-[70px] shadow-md bg-[#17455A] flex justify-between items-center">
      <aside className="flex justify-center items-center mr-[40px] ml-[40px]">
        <Link href="/" className="group">
          <Image
            className={`w-[60px] h-[50px] mr-[10px] ${hoverscale}`}
            src='/logo_gym.png'
            alt="logo del gimnasio"
            width={50}
            height={50}
          />
        </Link>
        <Link href="/" className={`mr-[20px] ${hoverLink}`}>GymHouse</Link>
        <Link href="/preguntas" className={`mr-[20px] ${hoverLink}`}>Preguntas Frecuentes</Link>
        <Link href="/nosotros" className={`mr-[20px] ${hoverLink}`}>Nosotros</Link>
      </aside>
      <div className="pr-[120px] flex-grow text-center">
        {isAuthenticated ? <h2 className="text-white">¡Bienvenido {nameUser}!</h2> : null}
      </div>
      <menu className="flex justify-center items-center mr-5">
        {isAuthenticated ? (
          <>
            <Link href="/rutinasGenerales" className={`mr-[10px] ${hoverLink}`}>Rutinas</Link>
            <Link href="/ejercicios" className={`mr-[10px] ${hoverLink}`}>Ejercicios</Link>
            <Link href="/perfil" className={`mr-[10px] ${hoverLink}`}>Perfil</Link>
            <input
              type="button"
              value="Cerrar Sesión"
              onClick={handleLogout}
              className={`ml-[40px] mr-[10px] ${hoverLink}`}
            />
          </>
        ) : (
          <>
            <Link href="/login" className={`mr-[10px] ${hoverLink}`}>Login</Link>
            <Link href="/register" className={`mr-[10px] ${hoverLink}`}>Register</Link>
          </>
        )}
      </menu>
    </header>
  );
};
