'use client';

import { useState, useEffect } from 'react';
import { useForm, SubmitHandler } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useRouter } from 'next/navigation';
import Swal from 'sweetalert2';
import Image from 'next/image';
import Link from 'next/link';
import { useTranslations } from 'next-intl';

import { boldFormText, btnIngresar, centerItem, hoverscale, inputForm } from '../tokens';
import { metadataLogin } from '../../components/metadata';
export { metadataLogin } from '../../components/metadata';

import { Login } from '@/types/login';
import { postLogin } from '@/libs/api_general';
import { loginSchema } from "@/validators/loginSchema";
import Spinner from '../../components/molecules/Spinner';

export default function LoginP() {
    const router = useRouter();
    const [loading, setLoading] = useState(true); 
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<Login>({
        resolver: zodResolver(loginSchema),
    });

    const t = useTranslations("login");
    const b = useTranslations("messages");


    useEffect(() => {
        if (localStorage.getItem('auth') === 'true') {
            router.push('/');
        } else {
            setLoading(false);
        }
    }, [router]);

    const onSubmit: SubmitHandler<Login> = async (data) => {
        setLoading(true); 

        const body = {
            email: data.email,
            password: data.password,
        };

        try {
            const token = await postLogin(body);

            if (token) {
                localStorage.setItem('token', token);
                localStorage.setItem('auth', 'true');
                Swal.fire({
                    title: `!${b("welcome")}!`,
                    text: `${b("success1")}`,
                    icon: "success",
                });
                router.push('/');
            } else {
                throw new Error("Login failed");
            }
        } catch (error) {
            Swal.fire({
                title: `!${b("error")}!`,
                text: `${b("failed1")}`,
                icon: "error",
            });
        } finally {
            setLoading(false); // Finaliza la carga tras el intento de autenticación
        }
    };

    if (loading) {
        return <Spinner />; // Muestra el Spinner mientras está cargando
    }

    return (
        <>
            <meta name="description" content={metadataLogin.description ?? ''} />
            <title>{metadataLogin.title?.toString() ?? ''}</title>

            <div className={`min-h-screen ${centerItem} flex-col`}>
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
                        {t("message")}
                    </h1>
                </div>
                <form className={`${inputForm} p-4 rounded-2xl border border-gray-500`} onSubmit={handleSubmit(onSubmit)}>
                    <div className="flex flex-col mb-4">
                        <label className="text-white" htmlFor="email">{t("email")}</label>
                        <input
                            {...register("email")}
                            id="email"
                            type="text"
                            className="p-2 rounded text-black"
                        />
                        {errors.email && <p className="text-red-500">{errors.email.message}</p>}
                    </div>
                    <div className={`${inputForm}`}>
                        <label className="text-white" htmlFor="password">{t("password")}</label>
                        <input
                            {...register("password")}
                            id="password"
                            type="password"
                            className="p-2 rounded text-black"
                        />
                        {errors.password && <p className="text-red-500">{errors.password.message}</p>}
                    </div>
                    <div className="mt-5">
                        <input
                            type="submit"
                            value={t("loginButton")}
                            className={`${btnIngresar} w-full`}
                        />
                    </div>
                </form>
            </div>
        </>
    );
}
