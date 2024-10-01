"use client";
import Image from 'next/image';
import Link from 'next/link';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { hoverscale , hoverLink} from '../tokens';

export const HeaderRoutines = () => {
    /* const [isAuthenticaded, setIsAuthenticated] = useState(false);
    const router = useRouter();

    useEffect(() => {
        const loggedIn = localStorage.getItem('isAuthenticated') === 'true';
        setIsAuthenticated(loggedIn);
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('isAuthenticated');
        setIsAuthenticated(false);
        router.push('/');
    }; */

    return (
        <header className="flex flex-row items-center justify-center w-full bg-[#011627] m-0 p-4">
                <input 
                    type="text" 
                    placeholder="Buscar" 
                    className="w-[10%] h-[50px] rounded-[20px] m-[20px]"
                />
                <Link href="/rutinasGenerales" className={`mr-[20px] ${hoverLink}`}>Rutinas generales</Link>
                <Link href="/rutinasProfesionales" className={`mr-[20px] ${hoverLink}`}>Rutinas profesionales</Link>
                <Link href="/rutinasUsuarios" className={`mr-[20px] ${hoverLink}`}>Rutinas de usuarios</Link>
                <Link href="/rutinasTodas" className={`mr-[20px] ${hoverLink}`}>Todas las rutinas</Link>
                <Link href="/rutinasMias" className={`mr-[20px] ${hoverLink}`}>Mis rutinas</Link>
        </header>
    )
}