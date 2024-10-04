import { z } from 'zod'

export const loginSchema = z.object({
    email: z.string()
        .email({ message: "Correo inválido" })
        .min(5, { message: "El campo debe tener minimo 5 caracteres." })
        .max(50, { message: "El campo no puede superar los 50 caracteres." }),
        
    password: z.string()
                .max(30, { message: "El campo no puede superar los 30 caracteres" })
})
