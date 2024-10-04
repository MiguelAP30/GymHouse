import { z } from 'zod';

export const loginSchema = z.object({
    email: z.string()        
        .min(1, { message: "El campo no puede estar vacio." })
        .max(50, { message: "El campo no puede superar los 50 caracteres." })
        .email({ message: "Correo inválido" }),
        
    password: z.string()
        .max(30, { message: "El campo no puede superar los 30 caracteres" })
        .min(1, { message: "El campo no puede estar vacío." })
});
