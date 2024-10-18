import { create } from 'zustand';

interface AuthState {
  isAuthenticated: boolean;
  token: string | null;
  nameUser: string | null;
  rol: number | null;
  setIsAuthenticated: (value: boolean) => void;
  setToken: (token: string | null) => void;
  fetchToken: () => Promise<void>;
}

const useAuthStore = create<AuthState>((set, get) => ({
  isAuthenticated: false,
  token: null,
  nameUser: null,
  rol: null,
  
  // Actualiza el estado de isAuthenticated al cambiarlo manualmente
  setIsAuthenticated: (value: boolean) => set({ isAuthenticated: value }),
  
  // Establece el token y marca al usuario como autenticado
  setToken: (token: string | null) => {
      set({ token, isAuthenticated: true });  // Autentica si hay token
  },
  
  // Recupera el token desde el localStorage y actualiza el estado de autenticación
  fetchToken: async () => {
    const token = get().token;
    if (token) {
      try {
        const response = await fetch('http://localhost:8000/api/v1/user_data', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        });
        const data = await response.json();
        console.log(data);
        
        // Al recibir los datos, actualiza el nombre y el rol
        set({ 
          nameUser: data.data["user.name"],
          rol: data.data["user.role"],
          isAuthenticated: true // Marca al usuario como autenticado
        });
        
        console.log(data.data["user.name"]);
        console.log("rol", data.data["user.role"]);
        
      } catch (error) {
        console.error("Error fetching user data:", error);
        // Si falla la autenticación, se marca como no autenticado
        set({ isAuthenticated: false });
      }
    } else {
      // Si no hay token, marca como no autenticado
      set({ isAuthenticated: false });
    }
  },
}));

export default useAuthStore;

