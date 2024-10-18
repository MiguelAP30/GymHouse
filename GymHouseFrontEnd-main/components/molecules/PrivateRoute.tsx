import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

interface PrivateRouteProps {
  role: string;
  token: string;
}

const PrivateRoute = ({ role, token }: PrivateRouteProps) => {
  if (!token) {
    // Si no hay token, redirigir al login
    return <Navigate to="/login" />;
  }

  if (!role) {
    // Si el rol del usuario no está permitido, redirigir a una página de "No autorizado"
    return <Navigate to="/unauthorized" />;
  }

  // Si el rol es correcto, renderizar el componente hijo (Outlet)
  return <Outlet />;
};

export default PrivateRoute;
