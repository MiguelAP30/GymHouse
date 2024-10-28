'use client'
import { useParams } from "next/navigation"
import { CardDia } from '../../../..../../../../components/organisms/cardDay'
import {centerItem} from '../../../../../components/tokens'

export default function DetailRoutine() {
const { detailsRoutine } = useParams()
    return (
        <section className={`${centerItem} flex-grow w-full bg-[#011627] m-0 p-4`}>
            <div className={ `${centerItem} flex flex-wrap bg-white rounded-[20px] `}>
                <CardDia idCard='E1'/>
                <CardDia idCard='E2'/>
                <CardDia idCard='E3'/>
                <CardDia idCard='E4'/>
                <CardDia idCard='E5'/>
                {detailsRoutine}
            </div>
        </section>
    )
}