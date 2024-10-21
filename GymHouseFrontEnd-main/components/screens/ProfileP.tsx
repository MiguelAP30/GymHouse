'use client';
import { useState, useEffect } from 'react';
import { TextTitle } from '@/components/tokens';
import { useForm, SubmitHandler } from 'react-hook-form';
import { zodResolver } from "@hookform/resolvers/zod";
import { profileSchema } from "@/validators/profileSchema";
import { postProfile, getProfileByEmail, getUserDataByEmail } from '@/libs/api_general';
import { Profile } from '@/types/profile';
import { User } from '@/types/user';
import Swal from 'sweetalert2';
import { useSearchParams } from 'next/navigation';
import useAuthStore from '@/validators/useAuthStore';

export default function ProfileP() {
    const searchParams = useSearchParams();
    const { fetchToken, setToken, email } = useAuthStore();
    const [profile, setProfile] = useState<Profile | null>(null);
    const [user, setUser] = useState<User | null>(null);
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
                    title: "¡Perfil actualizado!",
                    text: "Perfil actualizado correctamente",
                    icon: "success"
                });
            } else {
                throw new Error("No data in response");
            }
        } catch (error) {
            console.error("Error updating profile:", error);
            Swal.fire({
                title: "!Error!",
                text: "El perfil no ha podido actualizarse",
                icon: "error"
            });
        }
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <main className="w-full flex justify-between m-0 p-0">
            <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
                <h1 className={`${TextTitle}`}>Perfil</h1>
                <div className='w-1/2 flex justify-center items-center mb-[30px]'>
                    {profile ? (
                        <div className="flex flex-col justify-center items-center gap-4 p-4 bg-white rounded shadow-md">
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Email</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.email}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Número de Identidad</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.id_number}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Username</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.user_name}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Nombre</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.name}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Teléfono</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.phone}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Dirección</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.address}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Edad</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.birth_date}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Género</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{user?.gender}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Peso</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{profile.weight}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Altura</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{profile.height}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Actividad física</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{profile.physical_activity}</p>
                            </div>
                            <div className="flex flex-row">
                                <label className="mb-2 text-sm font-semibold text-gray-700 mt-[10px] mr-[5px]">Fecha</label>
                                <p className="p-2 border border-gray-300 rounded text-black">{profile.date}</p>
                            </div>
                        </div>
                    ) : (
                        <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4 p-4 bg-white rounded shadow-md">
                            <div className="flex flex-col">
                                <label className="mb-2 text-sm font-semibold text-gray-700" htmlFor="weight">Peso</label>
                                <input 
                                    type="number" 
                                    {...register("weight", { valueAsNumber: true })} 
                                    id="weight"
                                    className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                                />
                                {errors.weight && <span className="text-red-500 text-sm">{errors.weight.message}</span>}
                            </div>
                            <div className="flex flex-col">
                                <label className="mb-2 text-sm font-semibold text-gray-700" htmlFor="height">Altura</label>
                                <input 
                                    type="number" 
                                    {...register("height", { valueAsNumber: true })} 
                                    id="height"
                                    className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                                />
                                {errors.height && <span className="text-red-500 text-sm">{errors.height.message}</span>}
                            </div>
                            <div className="flex flex-col">
                                <label className="mb-2 text-sm font-semibold text-gray-700" htmlFor="physical_activity">Actividad física</label>
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
                                value="Actualizar"
                                className="p-2 mt-4 text-white bg-blue-500 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                        </form>
                    )}
                </div>
            </aside>
        </main>
    );
}