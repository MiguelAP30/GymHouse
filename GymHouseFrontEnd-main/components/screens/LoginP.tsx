'use client'

import Image from 'next/image';
import Link from 'next/link';

import { useForm, SubmitHandler } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import {boldFormText, btnIngresar, centerItem, hoverscale, inputForm} from '../tokens';
import { metadataLogin } from '@/components/metadata';
export { metadataLogin } from '@/components/metadata';
import { Login } from '@/types/login';
import { postLogin } from '@/libs/api_general';
import { useRouter } from 'next/navigation';
import Swal from 'sweetalert2';
import { loginSchema } from "@/validators/loginSchema"

export default function LoginP() {
    const router = useRouter();
    const {
            register,
            handleSubmit,
            watch,
            formState: { errors },
        } = useForm<Login>({
            resolver: zodResolver(loginSchema)
        })
        const onSubmit: SubmitHandler<Login> = async (data) => {
        console.log(data)
        const body = {
            email: data.email,
            password: data.password
        }
        let token = null
        token = await postLogin(body)
        console.log(await postLogin(body));
        if(token){
            localStorage.setItem('token', token);
            router.push('/')
            Swal.fire({
                title: "!Bienvenido!",
                text: "Usuario logueado correctamente",
                icon: "success"
            });
        } else{
            Swal.fire({
                title: "!Error!",
                text: "El usuario no ha podido loguearse",
                icon: "error"
            });
        }
    }



    return (
        <>
        <meta name="description" content={metadataLogin.description ?? ''} />
        <title>{metadataLogin.title?.toString() ?? ''}</title>

        
        <div className={`min-h-screen  ${centerItem} flex-col`} >
            <div className={`mb-5 ${centerItem} flex-col`}>
                <Link href="/">
                    <Image 
                        className={hoverscale}
                        src='/logo_gym.png'
                        alt="logo del gimnasio" 
                        width={350}
                        height={300}
                    />
                </Link>
                <h1 className={`${boldFormText}`}>
                    Welcome to GymHouse
                </h1>
            </div>
            <form className={`${inputForm} p-4 rounded-2xl border border-gray-500`} onSubmit={handleSubmit(onSubmit)}>
                <div className="flex flex-col mb-4">
                    <label className="text-white" htmlFor="user">Email</label>
                    <input 
                        {...register("email", { required: true })}
                        id="email" 
                        type="text" 
                        className="p-2 rounded text-black" 
                    />
                    {errors && <p className="text-red-500">{}</p>}
                </div>
                <div className={`${inputForm}`}>
                    <label className="text-white" htmlFor="password">Password</label>
                    <input 
                        {...register("password", { required: true })}
                        id="password" 
                        type="password" 
                        className="p-2 rounded text-black" 
                    />
                    {errors && <p className="text-red-500">{}</p>}
                </div>
                <div className="mt-5">
                    <input
                        type="submit"
                        value="Ingresar"
                        className={`${btnIngresar} w-full`}
                    />
                </div>
            </form>
        </div>
        </>
    );
}