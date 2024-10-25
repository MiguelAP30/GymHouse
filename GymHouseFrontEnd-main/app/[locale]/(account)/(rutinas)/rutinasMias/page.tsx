import type { Metadata } from "next";
import { centerItem} from '../../../../../components/tokens'
import { CardRutina } from '../../../../../components/organisms/CardRutina'

export const metadata: Metadata = {
    title: "Routines",
    description: "Saved routines by the user"
};

export default function selfRoutines() {
    return (
        <section className={` ${centerItem} flex-grow w-full bg-[#011627] m-0 p-4`}>
            <div className={ `${centerItem} flex flex-wrap bg-white rounded-[20px] `}>
                <CardRutina idCard='cardNumber1'/>
                <CardRutina idCard='cardNumber2'/>
                <CardRutina idCard='cardNumber3'/>
                <CardRutina idCard='cardNumber4'/>
                <CardRutina idCard='cardNumber5'/>
            </div>
        </section>
    );
}