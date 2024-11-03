'use client';
import { useState, useEffect } from 'react';
import { CardRutina } from "@/components/organisms/CardRutina";
import { Seaweed_Script } from 'next/font/google';
import { hoverscale } from '@/components/tokens';
import Image from "next/image"

export default function admin() {
    return (
        <main className="w-full flex justify-center bg-[#011627] min-h-full">
            <section className="w-full flex flex-col items-center bg-[#296ca3] rounded-lg p-4">
                <p className="flex gap-2 items-center">
                    <Image
                        className={"rounded-md " + hoverscale}
                        src='/logo_gym.png'
                        alt='Logo Gym'
                        width='250'
                        height='200'
                    />
                    Client
                </p>
                <section className="flex flex-col p-4 bg-[#296ca3] rounded-lg w-full">
                    <form className="w-full flex justify-between mb-4">
                        <div className="flex items-center gap-2">
                            <select name="" id="" className="border rounded p-2">
                                <option value="10">10</option>
                            </select>
                            <p>Entries per page</p>
                        </div>
                        <div>
                            <input placeholder="Search" type="text" className="border rounded p-2" />
                        </div>
                    </form>
                    <table className="w-full border-collapse">
                        <thead>
                            <tr>
                                <th className="border p-2">Name</th>
                                <th className="border p-2">Position</th>
                                <th className="border p-2">Office</th>
                                <th className="border p-2">Age</th>
                                <th className="border p-2">Start date</th>
                                <th className="border p-2">Salary</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td className="border p-2">My Name</td>
                                <td className="border p-2">Admin</td>
                                <td className="border p-2">Off Manizales</td>
                                <td className="border p-2">25</td>
                                <td className="border p-2">Hoy</td>
                                <td className="border p-2">00000001</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </section>
        </main>
    );
}
