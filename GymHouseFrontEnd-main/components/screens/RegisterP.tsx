'use client';
import Image from 'next/image';
import Link from 'next/link';
import { boldFormText, btnIngresar, centerItem, hoverscale, inputForm } from '../tokens';
import { metadataRegister } from '@/components/metadata';
import { useForm, SubmitHandler } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod"
import { Register } from '@/types/register';
import { useState } from 'react';
import { postRegister } from '@/libs/api_general';
import Swal from 'sweetalert2';
import { useRouter } from 'next/navigation';
import { registerSchema } from "@/validators/registerSchema"
import { log } from 'console';

export default function RegisterP() {
    const router = useRouter();
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm<Register & { confirm_password: string }>({
        resolver: zodResolver(registerSchema)
    }); // Se incluye confirm_password solo en el formulario

    const onSubmit: SubmitHandler<Register> = async (data) => {
        console.log(data);
        const dataregister: Register = {
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
        setRegister(dataregister);
        const register =await postRegister(dataregister); 
        if(register.data){
        router.push('/')
        Swal.fire({
            title: "!Bienvenido!",
            text: "Usuario creado correctamente",
            icon: "success"
        });
        }else{
            Swal.fire({
                title: "!Error!",
                text: "El usuario no ha podido crearse",
                icon: "error"
            });
        }
    };

    const password = watch("password");
    const confirmPassword = watch("confirm_password");
    const [Register, setRegister] = useState<Register>();

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
                        Welcome to GymHouse
                    </h1>
                </div>
                <form className={`${inputForm} p-4 rounded-2xl border border-gray-500`} onSubmit={handleSubmit(onSubmit)}>
                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="email">Email</label>
                            <input
                                {...register("email")}
                                id="email"
                                type="email" 
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.email && <p className='text-red-500'>{errors.email.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="id_number">Número de Identificación</label>
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
                            <label className="text-white" htmlFor="password">Contraseña</label>
                            <input
                                {...register("password")}
                                id="password"
                                type="password"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.password && <p>{errors.password.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="confirm_password">Confirmar contraseña</label>
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

                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="name">Nombre</label>
                            <input
                                {...register("name")}
                                id="name"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.name && <p>{errors.name.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="username">Nombre de Usuario</label>
                            <input
                                {...register("username")}
                                id="username"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.username && <p>{errors.username.message}</p>}
                        </div>
                    </div>

                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="phone">Teléfono</label>
                            <input
                                {...register("phone")}
                                id="phone"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.phone && <p>{errors.phone.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="address">Dirección (opcional)</label>
                            <input
                                {...register("address")}
                                id="address"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                        </div>
                    </div>

                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="birth_date">Fecha de Nacimiento</label>
                            <input
                                {...register("birth_date")}
                                id="birth_date"
                                type="date"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.birth_date && <p>{errors.birth_date.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="gender">Género</label>
                            <select
                                {...register("gender")}
                                id="gender"
                                className="text-black p-2 rounded w-full"
                            >
                                <option value="">Seleccione su género</option>
                                <option value="m">Masculino</option>
                                <option value="f">Femenino</option>
                            </select>
                            {errors.gender && <p>{errors.gender.message}</p>}
                        </div>
                    </div>

                    <div className="mt-5">
                        <input
                            type="submit"
                            value="Registrar"
                            className={`${btnIngresar} w-full`}
                        />
                    </div>
                </form>
            </div>
        </>
    );
}