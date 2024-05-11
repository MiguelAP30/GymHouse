import React, { useState, useEffect } from 'react';

const MyRoutines = () => {
    const [routines, setRoutines] = useState([]);

    useEffect(() => {
        // Aquí puedes hacer una llamada a la API para obtener las rutinas del usuario
        // y luego actualizar el estado con setRoutines
    }, []);

    return (
        <div>
            <h1>Mis Rutinas</h1>
            {routines.length === 0 ? (
                <p>No tienes rutinas</p>
            ) : (
                <ul>
                    {routines.map((routine) => (
                        <li key={routine.id}>{routine.name}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default MyRoutines;