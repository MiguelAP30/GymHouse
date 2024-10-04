"use client";
import Image from 'next/image';
import Link from 'next/link';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { hoverscale , hoverLink} from '../tokens';

export const Header = () => {
    const [isAuthenticaded, setIsAuthenticated] = useState(false);
    const [nameUser, setNameUser] = useState("");

    const router = useRouter();

    useEffect(() => {
        const loggedIn = localStorage.getItem('token');
        if(!!loggedIn){
            showNameUser(loggedIn)
        }
        setIsAuthenticated(!!loggedIn);
    }, []);

    const showNameUser = async(token:string) => {
        fetch('http://localhost:8000/api/v1/user_data', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        }).then(response => response.json()).then((data)=>{
            setNameUser(data.data["user.name"]);
            console.log(data.data["user.name"]);
            
        })
    }

    const handleLogout = () => {
        localStorage.removeItem('token');
        setIsAuthenticated(false);
        router.push('/');
    };

    return (
        <header className="w-full max-w-full h-[70px] shadow-md bg-[#17455A] flex justify-between items-center ">
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
                {isAuthenticaded ? <h2 className="text-white">! Bienvenido {nameUser} !</h2> : null}
            </div>
            <menu className="flex justify-center items-center mr-5">
                {isAuthenticaded ? 
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
                : 
                    <>
                        <Link href="/login" className={`mr-[10px] ${hoverLink}`}>Login</Link>
                        <Link href="/register" className={`mr-[10px] ${hoverLink}`}>Register</Link>
                    </>
                }
            </menu>
        </header>
    )
}
