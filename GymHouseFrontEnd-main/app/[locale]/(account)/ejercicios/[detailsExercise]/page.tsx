'use client'
import { useParams } from "next/navigation"
import {TextTitle, TextParagraph} from '../../../../components/tokens'
import Image from "next/image"

export default function DetailRoutine() {

const { detailsExercise } = useParams()

return (
    <main className="w-full flex justify-between min-h-[80vh] h-[80vh] m-0 p-0">
        <aside className="flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-0">
            <h1 className={`${TextTitle}`}>
                Ejercicio {detailsExercise}
            </h1>
            <Image
                className={"rounded-md "}
                src='/ejercicios.png'
                alt='Logo Gym'
                width='1200'
                height='400'
            />
            <p className={`${TextParagraph}`}>
                Este es el ejercicio {detailsExercise} que sirve para...
            </p>
        </aside>
    </main>
)
}