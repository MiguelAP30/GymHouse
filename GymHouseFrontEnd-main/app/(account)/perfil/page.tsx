import type { Metadata } from "next";
import {TextTitle, TextParagraph} from '../../../components/tokens'

export const metadata: Metadata = {
    title: "Profile",
    description: "Profile is for people that want to see their profile."
};

export default function profile() {
    return (
        <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
            <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
                <h1 className={`${TextTitle}`}>
                    Perfil
                </h1>
                <p className={`${TextParagraph}`}>
                    Perfil para personas que quieren ver su progreso en el fitness.
                </p>
            </aside>
        </main>
    );
}