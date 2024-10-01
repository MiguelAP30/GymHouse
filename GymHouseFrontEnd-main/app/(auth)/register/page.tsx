'use client';
import Image from 'next/image';
import Link from 'next/link';
import { boldFormText, btnIngresar, centerItem, hoverscale, inputForm } from '../../../components/tokens';
import { metadataRegister } from '@/components/metadata';
import { useForm, SubmitHandler } from "react-hook-form";
import { Register } from '@/types/register';
import { useState } from 'react';
import { postRegister } from '@/libs/api_general';
import Swal from 'sweetalert2';
import { useRouter } from 'next/navigation';

export default function register() {
    const router = useRouter();
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm<Register & { confirm_password: string }>(); // Se incluye confirm_password solo en el formulario

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

    const password = watch("password"); // Observa el valor del campo de contraseña
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
                            {...register("email", {
                                required: "El correo es obligatorio",
                                validate: (value) => {
                                const isValidEmail = value.includes("@") && value.includes(".");
                                return isValidEmail || "Ingresa un correo válido";
                                },
                            })}
                            id="email"
                            type="email" 
                            className="text-black p-2 rounded w-full"
                            />
                            {errors.email && <p className='text-red-500'>{errors.email.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="id_number">Número de Identificación</label>
                            <input
                                {...register("id_number", { required: "La identificación es obligatoria",
                                    minLength: {
                                        value: 6,
                                        message: "La identificación debe tener al menos 6 caracteres"
                                    },
                                    maxLength: {
                                        value: 10,
                                        message: "La identificación no puede exceder los 10 caracteres"
                                    }
                                 })}
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
                                {...register("password", { required: "La contraseña es obligatoria",
                                    minLength: {
                                        value: 6,
                                        message: "La contraseña debe tener al menos 6 caracteres"
                                    },
                                    maxLength: {
                                        value: 10,
                                        message: "La contraseña no puede exceder los 10 caracteres"
                                    }
                                 })}
                                id="password"
                                type="password"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.password && <p>{errors.password.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="confirm_password">Confirmar contraseña</label>
                            <input
                                {...register("confirm_password", {
                                    required: "Confirma tu contraseña",
                                    validate: value => value === password || "Las contraseñas no coinciden"
                                })}
                                id="confirm_password"
                                type="password"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.confirm_password && <p>{errors.confirm_password.message}</p>}
                        </div>
                    </div>

                    <div className="flex flex-wrap -mx-2 mb-4">
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="name">Nombre</label>
                            <input
                                {...register("name", { required: "El nombre es obligatorio",
                                    minLength: {
                                        value: 2,
                                        message: "El nombre debe tener almenos 2 caracteres"
                                    },
                                    maxLength: {
                                        value: 50,
                                        message: "El nombre no puede exceder los 50 caracteres"
                                    }
                                 })}
                                id="name"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.name && <p>{errors.name.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2">
                            <label className="text-white" htmlFor="username">Nombre de Usuario</label>
                            <input
                                {...register("username", { required: "El nombre de usuario es obligatorio",
                                    minLength: {
                                        value: 6,
                                        message: "El nombre de usuario debe tener almenos 2 caracteres"
                                    },
                                    maxLength: {
                                        value: 60,
                                        message: "El nombre de usuario no puede exceder los 50 caracteres"
                                    }
                                 })}
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
                                {...register("phone", { required: "El teléfono es obligatorio",
                                    minLength: {
                                        value: 6,
                                        message: "El telefono debe tener almenos 6 caracteres"
                                    },
                                    maxLength: {
                                        value: 20,
                                        message: "El telefono no puede exceder los 20 caracteres"
                                    }
                                 })}
                                id="phone"
                                type="text"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.phone && <p>{errors.phone.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="address">Dirección (opcional)</label>
                            <input
                                {...register("address",{
                                    minLength: {
                                        value: 6,
                                        message: "La direccion debe tener almenos 6 caracteres"
                                    },
                                    maxLength: {
                                        value: 150,
                                        message: "La direccion no puede exceder los 150 caracteres"
                                    }
                                })}
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
                                {...register("birth_date", { required: "La fecha de nacimiento es obligatoria" })}
                                id="birth_date"
                                type="date"
                                className="text-black p-2 rounded w-full"
                            />
                            {errors.birth_date && <p>{errors.birth_date.message}</p>}
                        </div>
                        <div className="w-full md:w-1/2 px-2 mb-4 md:mb-0">
                            <label className="text-white" htmlFor="gender">Género</label>
                            <select
                                {...register("gender", { required: "El género es obligatorio" })}
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
