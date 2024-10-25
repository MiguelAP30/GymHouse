import type { Metadata } from "next";
import {TextTitle, TextParagraph, centerItem} from '../../../../components/tokens'
import { CardRutina } from '../../../../components/organisms/CardRutina'

export const metadata: Metadata = {
    title: "Routines",
    description: "General routines for people"
};

export default function generalRoutines() {
    return (
        <section className={`${centerItem} flex-grow w-full bg-[#011627] m-0 p-4`}>
            <div className={ `${centerItem} flex flex-wrap bg-white rounded-[20px] `}>
                <CardRutina idCard='R1'/>
                <CardRutina idCard='R2'/>
                <CardRutina idCard='R3'/>
                <CardRutina idCard='R4'/>
                <CardRutina idCard='R5'/>
            </div>
        </section>
    );
}