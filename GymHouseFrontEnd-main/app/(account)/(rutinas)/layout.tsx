import type { Metadata } from "next";
import {HeaderRoutines} from '../../../components/molecules/Header_routines'
import { CardRutina } from '../../../components/organisms/CardRutina'

export const metadata: Metadata = {
    title: "Routines",
    description: "Routines"
};

export default function AuthLayout({
    children
}: {
    children: React.ReactNode;
}) {
    return (
        <>
        <div className="flex flex-col min-h-screen">
            <main className="flex-grow w-full flex flex-col m-0 p-0">
                <HeaderRoutines/>
                {children}
            </main>
        </div>
        </>
    );
}