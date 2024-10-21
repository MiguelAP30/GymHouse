import { z } from 'zod';

export const profileSchema = z.object({
    weight: z.number().min(0, "El peso debe ser un número positivo"), // Asegura que el peso sea un número positivo
    height: z.number().min(0, "La altura debe ser un número positivo"), // Asegura que la altura sea un número positivo
    physical_activity: z.number().min(0, "La actividad física debe ser un número positivo") // Asegura que la actividad física sea un número positivo
});
