import type { Metadata } from "next";
import {TextTitle, TextParagraph, centerItem} from '../../../components/tokens'

export const metadata: Metadata = {
    title: "GymHouse",
    description: "Gymahouse is fantastic.",
};

export default function About() {
    return (
        <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
            <aside className={`${centerItem} w-full bg-[#011627] m-0 p-0`}>
                <h1 className={`${TextTitle}`}>
                    ¿Quienes somos?
                </h1>
                <p className={`${TextParagraph}`}>
                    Somos un grupo de entusiastas del fitness que se unieron para crear GymHouse, 
                    un lugar donde puedes encontrar rutinas de ejercicios personalizadas y mucho más.
                </p>
            </aside>
        </main>
    );
}