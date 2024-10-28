'use client';
import { useState, useEffect } from 'react';
import { centerItem } from '../../../../../components/tokens';
import { CardRutina } from "@/components/organisms/CardRutina";
import { get_training_plans_by_role_premium } from "@/libs/api_general";
import { training_plan } from "@/types/training_plan";

export default function GeneralRoutines() {
    const [trainingPlans, setTrainingPlans] = useState<training_plan[]>([]);
    const [loading, setLoading] = useState(true);
    const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;

    useEffect(() => {
        const fetchTrainingPlans = async () => {
            if (token) {
                try {
                    const plans = await get_training_plans_by_role_premium(token);
                    setTrainingPlans(plans);
                } catch (error) {
                    console.error("Error fetching training plans:", error);
                } finally {
                    setLoading(false);
                }
            }
        };
        fetchTrainingPlans();
    }, [token]);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <section className={`${centerItem} flex-grow w-full bg-[#011627] m-0 p-4`}>
            <div className={`${centerItem} flex flex-wrap bg-white rounded-[20px]`}>
                {trainingPlans.length > 0 ? (
                    trainingPlans.map((training_plan, index) => (
                        <CardRutina key={index} trainingPlan={training_plan} />
                    ))
                ) : (
                    <div>No training plans available.</div>
                )}
            </div>
        </section>
    );
}