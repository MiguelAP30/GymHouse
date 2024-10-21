'use client';
import { Header, Footer } from '@/components';
import useAuthStore from '@/validators/useAuthStore';
import { useParams } from 'next/navigation';
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Spinner from '@/components/molecules/Spinner';

export default function AccountLayout({
    children
  }: {
    children: React.ReactNode;
  }) {
    const { isAuthenticated, fetchToken, rol, setToken } = useAuthStore();
    const [loading, setLoading] = useState(true);
    const router = useRouter();
    const { id } = useParams();

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
        if (!isAuthenticated || (rol ?? 0) < 2) {
          router.push("/"); // Redirige al home si no está autenticado o el rol no es correcto
        }
      }
    }, [isAuthenticated, rol, loading, router]);

    // Mientras se está verificando la autenticación, muestra el Spinner
    if (loading) {
      return <Spinner />;
    }

    // Si pasa la verificación de autenticación y permisos, renderiza el contenido
    if (isAuthenticated && (rol ?? 0) > 1) {
      return (
        <div>
          <Header />
          { children }
          <Footer />
        </div>
      );
    }
}