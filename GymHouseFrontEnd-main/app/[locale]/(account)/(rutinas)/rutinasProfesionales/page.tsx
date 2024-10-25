import type { Metadata } from "next";
import {centerItem} from '../../../../../components/tokens'
import { CardRutina } from '../../../../../components/organisms/CardRutina'

export const metadata: Metadata = {
    title: "Routines",
    description: "Routines created by professionals"
};

export default function professionalRoutines() {
    return (
        <section className={`${centerItem} flex-grow w-full bg-[#011627] m-0 p-4 `}>
            <div className="flex flex-wrap items-center justify-center bg-white rounded-[20px] ">
                <CardRutina idCard='cardNumber1'/>
                <CardRutina idCard='cardNumber2'/>
                <CardRutina idCard='cardNumber3'/>
                <CardRutina idCard='cardNumber4'/>
                <CardRutina idCard='cardNumber5'/>
            </div>
        </section>
    );
}