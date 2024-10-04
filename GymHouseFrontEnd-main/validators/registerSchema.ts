import { z } from 'zod'

export const registerSchema = z.object({
    email: z.string()
        .email({ message: "Debe ser un correo válido" })
        .min(5, { message: "El campo debe tener mínimo 5 caracteres." })
        .max(50, { message: "El campo no puede superar los 50 caracteres." }),

    id_number: z.string()
        .length(10, { message: "El campo debe tener exactamente 10 caracteres" })
        .regex(/^[0-9]+$/, { message: "El número de identificación debe contener solo números." }),

    password: z.string()
        .min(8, { message: "La contraseña debe tener mínimo 8 caracteres." })
        .max(30, { message: "La contraseña no puede superar los 30 caracteres." })
        .regex(/[A-Z]/, { message: "La contraseña debe contener al menos una letra mayúscula." })
        .regex(/[0-9]/, { message: "La contraseña debe contener al menos un número." }),
    
    confirm_password: z.string()
        .min(8, { message: "La contraseña debe tener mínimo 8 caracteres." })
        .max(30, { message: "La contraseña no puede superar los 30 caracteres." })
        .regex(/[A-Z]/, { message: "La contraseña debe contener al menos una letra mayúscula." })
        .regex(/[0-9]/, { message: "La contraseña debe contener al menos un número." }),

    username: z.string()
        .min(5, { message: "El nombre de usuario debe tener mínimo 5 caracteres." })
        .max(30, { message: "El nombre de usuario no puede superar los 30 caracteres." }),

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
        .regex(/^\d{2}-\d{2}-\d{4}$/, { message: "La fecha de nacimiento debe tener el formato DD-MM-YYYY." }),
    
    gender: z.string().optional()

}).refine((data) => data.password === data.confirm_password, {
    path: ['confirm_password'],
    message: "Las contraseñas no coinciden",
});
