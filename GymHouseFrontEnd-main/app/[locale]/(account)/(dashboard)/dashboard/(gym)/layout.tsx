'use client';
import useAuthStore from '@/validators/useAuthStore';
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Spinner from '@/components/molecules/Spinner';
import {role} from '@/types/roles';
import {HeaderDashboardGym} from '@/components/molecules/Header_Dashboard_gym';

export default function contenidoGym({
        children
    }: {
        children: React.ReactNode;
    }) {
        const { isAuthenticated, fetchToken, rol, setToken } = useAuthStore();
        const [loading, setLoading] = useState(true);
        const router = useRouter();
    
        // Obtiene el token desde localStorage
        const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
    
        useEffect(() => {
            const checkPermission = async () => {
            setLoading(true);
            setToken(token); // Establece el token en el store
            await fetchToken(); // Obtiene los datos del usuario
            setLoading(false); // Finaliza la carga
            };
            checkPermission();
        }, [fetchToken, setToken, token]);
    
        useEffect(() => {
            // Si ya se terminó la carga y no está autenticado o el rol no es el correcto, redirige
            if (!loading) {
            if (!isAuthenticated || (rol !== null && rol != role.gym)) {
                router.push("/"); // Redirige al home si no está autenticado o el rol no es correcto
            }
            }
        }, [isAuthenticated, rol, loading, router]);
    
        // Mientras se está verificando la autenticación, muestra el Spinner
        if (loading) {
            return <Spinner />;
        }
    
        // Si pasa la verificación de autenticación y permisos, renderiza el contenido
        if (isAuthenticated && (rol !== null && rol == role.gym)) {
            return (
                <div className="flex flex-1">
                    <HeaderDashboardGym />
                    {children}
                </div>
                
            );
        }
}