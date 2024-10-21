import { z } from 'zod'

export const profileSchema = z.object({
    name: z.string()
        .min(5, { message: "El nombre debe tener mínimo 5 caracteres." })
        .max(50, { message: "El nombre no puede superar los 50 caracteres." }),
    
    phone: z.string()
        .min(10, { message: "El número de teléfono debe tener mínimo 10 caracteres." })
        .max(15, { message: "El número de teléfono no puede superar los 15 caracteres." })
        .regex(/^\+?[0-9]+$/, { message: "El número de teléfono debe contener solo números y puede incluir el prefijo internacional." }),
    
    address: z.string()
        .min(5, { message: "La dirección debe tener mínimo 5 caracteres." })
        .max(100, { message: "La dirección no puede superar los 100 caracteres." })
        .optional(),
    
    birth_date: z.string()
})

