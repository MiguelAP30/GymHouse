import type { Metadata } from "next";
import {TextTitle, TextParagraph} from '../../../../components/tokens'
import { CardRutina } from '../../../../components/organisms/CardRutina'

export const metadata: Metadata = {
    title: "Routines",
    description: "Routines created by users"
};

export default function userRoutines() {
    return (
        <section className="flex-grow flex flex-col items-center justify-center w-full bg-[#011627] m-0 p-4">
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