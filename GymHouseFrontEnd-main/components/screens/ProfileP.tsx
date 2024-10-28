'use client';
import { useState, useEffect } from 'react';
import { TextTitle } from '../../components/tokens';
import { useForm, SubmitHandler } from 'react-hook-form';
import { zodResolver } from "@hookform/resolvers/zod";
import { profileSchema } from "@/validators/profileSchema";
import { postProfile, getProfileByEmail, getUserDataByEmail } from '@/libs/api_general';
import { Profile } from '@/types/profile';
import { User } from '@/types/user';
import Swal from 'sweetalert2';
import { useSearchParams } from 'next/navigation';
import useAuthStore from '@/validators/useAuthStore';
import { hoverscale } from '@/components/tokens';
import Image from 'next/image';
import { useTranslations } from 'next-intl';

export default function ProfileP() {
    const t = useTranslations("profile")
    const b = useTranslations("messages");
    const searchParams = useSearchParams();
    const { fetchToken, setToken, email } = useAuthStore();
    
    const [profile, setProfile] = useState<Profile >();
    const [user, setUser] = useState<User>();
    const [loading, setLoading] = useState(true);
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<Profile>({
        resolver: zodResolver(profileSchema)
    });

    const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;

    useEffect(() => {
        const fetchProfileAndUser = async () => {
            setToken(token);
            await fetchToken();
            if (email) {
                const profiles = await getProfileByEmail(email as string, token as string);
                if (profiles.length > 0) {
                    setProfile(profiles[0]); // Asume que tomas el primer perfil si hay más de uno
                }
                const userData = await getUserDataByEmail(email as string, token as string);
                setUser(userData);
                setLoading(false);
            }
        };
        fetchProfileAndUser();
    }, [email]);
    
    const onSubmit: SubmitHandler<Profile> = async (data) => {
        try {
            const profileData: Profile = {
                user_email: email as string,
                weight: data.weight,
                height: data.height,
                physical_activity: data.physical_activity,
                date: new Date().toLocaleDateString('sv-SE')
            };
            setProfile(profileData);

            const response = await postProfile(profileData, token as string);
            if (response) {
                Swal.fire({
                    title: `!${b("profile")}!`,
                    text: `${b("success3")}`,
                    icon: "success"
                });
            } else {
                throw new Error("No data in response");
            }
        } catch (error) {
            console.error("Error updating profile:", error);
            Swal.fire({
                title: `!${b("error")}!`,
                text: `${b("failed2")}`,
                icon: "error"
            });
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }
    return (
        <main className="w-full flex justify-center m-0 p-0 bg-[#011627] min-h-screen">
            <aside className="flex flex-col items-center justify-center w-full max-w-md px-6 py-8  shadow-lg rounded-lg">
                <h1 className="text-3xl font-semibold text-[#fefefe] mb-8">{t("title")}</h1>
                {profile ? (
                    <div className="flex flex-col items-center gap-6 p-8 rounded-md shadow-lg bg-gradient-to-br from-[#17455A] to-blue-800 bg-opacity-70">
                    <div className="w-32 h-32 rounded-full overflow-hidden mb-4">
                        <Image 
                            className={`object-cover w-full h-full ${hoverscale}`}
                            src='/logo_twitter.png'
                            alt="logo twitter" 
                            width={50}
                            height={50}
                        />
                    </div>
                
                    <h2 className="text-2xl font-semibold text-white">{user?.name}</h2>
                    <p className="text-sm font-light text-white mb-6">{user?.user_name}</p>
                
                    <div className="flex flex-col items-start w-full gap-4">
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("email")}</span>
                            <p className="text-white">{user?.email}</p>
                        </div>
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("idNumber")}</span>
                            <p className="text-white">{user?.id_number}</p>
                        </div>
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("phoneNumber")}</span>
                            <p className="text-white">{user?.phone}</p>
                        </div>
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("address")}</span>
                            <p className="text-white">{user?.address}</p>
                        </div>
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("birthdate")}</span>
                            <p className="text-white">{user?.birth_date}</p>
                        </div>
                        <div className="flex flex-row items-center justify-between w-full">
                            <span className="text-sm font-semibold text-white">{t("gender")}</span>
                            <p className="text-white">{user?.gender}</p>
                        </div>
                    </div>
                
                    <div className="flex flex-col items-center w-full gap-4 mt-4">
                        <button className="w-full py-2 text-white border border-white rounded-md  ">{t("weight")} {profile.weight}</button>
                        <button className="w-full py-2 text-white border border-white rounded-md  ">{t("height")} {profile.height}</button>
                        <button className="w-full py-2 text-white border border-white rounded-md  ">{t("activity")} {profile.physical_activity}</button>
                        <button className="w-full py-2 text-white border border-white rounded-md  ">{t("date")} {profile.date}</button>
                    </div>
                </div>
                
                ) : (
                    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4 p-4 bg-gradient-to-br from-[#37318a] to-blue-800 bg-opacity-70 rounded shadow-md">
                        <div className="flex flex-col ">
                            <label className="mb-2 text-sm font-semibold text-white" htmlFor="weight">{t("weight")}</label>
                            <input 
                                type="number" 
                                {...register("weight", { valueAsNumber: true })} 
                                id="weight"
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            />
                            {errors.weight && <span className="text-red-500 text-sm">{errors.weight.message}</span>}
                        </div>
                        <div className="flex flex-col">
                            <label className="mb-2 text-sm font-semibold text-white" htmlFor="height">{t("height")}</label>
                            <input 
                                type="number" 
                                {...register("height", { valueAsNumber: true })} 
                                id="height"
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            />
                            {errors.height && <span className="text-red-500 text-sm">{errors.height.message}</span>}
                        </div>
                        <div className="flex flex-col">
                            <label className="mb-2 text-sm font-semibold text-white" htmlFor="physical_activity">{t("activity")}</label>
                            <input 
                                type="number" 
                                {...register("physical_activity", { valueAsNumber: true })} 
                                id="physical_activity"
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            />
                            {errors.physical_activity && <span className="text-red-500 text-sm">{errors.physical_activity.message}</span>}
                        </div>
                        <input 
                            type="submit" 
                            value={t("button")}
                            className="p-2 mt-4 text-white bg-blue-500 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                    </form>
                )}
            </aside>
        </main>
    );
    
}