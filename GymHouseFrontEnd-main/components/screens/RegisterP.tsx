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
import { metadataRegister } from '@/components/metadata';
export { metadataRegister } from '@/components/metadata';

import { Register } from '@/types/register';
import { postRegister } from '@/libs/api_general';
import { registerSchema } from "@/validators/registerSchema";
import Spinner from '../../components/molecules/Spinner';

export default function RegisterP() {
    const router = useRouter();
    const [loading, setLoading] = useState(true); // Estado de carga

    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm<Register & { confirm_password: string }>({
        resolver: zodResolver(registerSchema)
    }); 

    const onSubmit: SubmitHandler<Register> = async (data) => {
        setLoading(true); // Inicia la carga cuando se envía el formulario

        const dataRegister: Register = {
            email: data.email,
            id_number: data.id_number,
            password: data.password,
            username: data.username,
            name: data.name,
            phone: data.phone,
            address: data.address,
            birth_date: data.birth_date,
            gender: data.gender
        };

        try {
            const registerResponse = await postRegister(dataRegister); 

            if (registerResponse.data) {
                Swal.fire({
                    title: "!Bienvenido!",
                    text: "Usuario creado correctamente",
                    icon: "success"
                });
                router.push('/login');
            } else {
                throw new Error("Registro fallido");
            }
        } catch (error) {
            Swal.fire({
                title: "!Error!",
                text: "El usuario no ha podido crearse",
                icon: "error"
            });
        } finally {
            setLoading(false); // Finaliza la carga tras el intento de registro
        }
    };

    const password = watch("password");
    const confirmPassword = watch("confirm_password");
    const t = useTranslations("register");

    // Verificar si el usuario ya está autenticado
    useEffect(() => {
        if (localStorage.getItem('auth') === 'true') {
            router.push('/');
        } else {
            setLoading(false); // Finaliza la carga si el usuario no está autenticado
        }
    }, [router]);

    if (loading) {
        return <Spinner />; // Muestra el Spinner mientras está cargando
    }

    return (
        <>
            <meta name="description" content={metadataRegister.description ?? ''} />
            <title>{metadataRegister.title?.toString() ?? ''}</title>

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
                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="email">{t("email")}</label>
                            <input
                                {...register("email")}
                                id="email"
                                type="email" 
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.email && <p className='text-red-500'>{errors.email.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="id_number">{t("idNumber")}</label>
                            <input
                                {...register("id_number")}
                                id="id_number"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.id_number && <p>{errors.id_number.message}</p>}
                        </div>
                    </div>
                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="password">{t("password")}</label>
                            <input
                                {...register("password")}
                                id="password"
                                type="password"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.password && <p>{errors.password.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="confirm_password">{t("repeatPassword")}</label>
                            <input
                                {...register("confirm_password")}
                                id="confirm_password"
                                type="password"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.confirm_password && <p>{errors.confirm_password.message}</p>}
                        </div>
                        {password !== confirmPassword && (
                            <p className='text-red-500'>Las contraseñas no coinciden</p>
                        )}
                    </div>
                    {/* Resto de los campos del formulario */}
                    <div className="mt-5">
                        <input
                            type="submit"
                            value={t("registerButton")}
                            className={`${btnIngresar} w-full`}
                        />
                    </div>
                </form>
            </div>
        </>
    );
}
