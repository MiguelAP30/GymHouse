'use client'

import Image from 'next/image';
import Link from 'next/link';

import { useForm, SubmitHandler } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { boldFormText, btnIngresar, centerItem, hoverscale, inputForm } from '../tokens';
import { metadataLogin } from '../../components/metadata';
export { metadataLogin } from '../../components/metadata';
import { Login } from '@/types/login';
import { postLogin } from '@/libs/api_general';
import { useRouter } from 'next/navigation';
import Swal from 'sweetalert2';
import { loginSchema } from "@/validators/loginSchema";
import { useTranslations } from 'next-intl';

export default function LoginP() {
    const router = useRouter();
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<Login>({
        resolver: zodResolver(loginSchema),
    });

    const onSubmit: SubmitHandler<Login> = async (data) => {
        console.log(data);
        const body = {
            email: data.email,
            password: data.password,
        };
        let token = null;
        token = await postLogin(body);
        console.log(await postLogin(body));
        if (token) {
            localStorage.setItem('token', token);
            router.push('/');
            Swal.fire({
                title: "!Bienvenido!",
                text: "Usuario logueado correctamente",
                icon: "success",
            });
        } else {
            Swal.fire({
                title: "!Error!",
                text: "El usuario no ha podido loguearse",
                icon: "error",
            });
        }
    };
    const t = useTranslations("login")
    return (
        <>
            <meta name="description" content={metadataLogin.description ?? ''} />
            <title>{metadataLogin.title?.toString() ?? ''}</title>

            <div className={`min-h-screen  ${centerItem} flex-col`}>
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
                        {/* Mostrar el mensaje de error para el email */}
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
                        {/* Mostrar el mensaje de error para el password */}
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
