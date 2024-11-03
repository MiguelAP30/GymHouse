'use client';
import { useState, useEffect } from 'react';
import { CardRutina } from "@/components/organisms/CardRutina";

export default function admin() {
    return (
        <main className="w-full flex justify-center bg-[#011627] min-h-full">
            <ul role="list" className="divide-y divide-gray-100">
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Leslie Alexander</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">leslie.alexander@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Co-Founder / CEO</p>
                    <p className="mt-1 text-xs/5 text-gray-500">Last seen <time datetime="2023-01-23T13:23Z">3h ago</time></p>
                    </div>
                </li>
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Michael Foster</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">michael.foster@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Co-Founder / CTO</p>
                    <p className="mt-1 text-xs/5 text-gray-500">Last seen <time datetime="2023-01-23T13:23Z">3h ago</time></p>
                    </div>
                </li>
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Dries Vincent</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">dries.vincent@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Business Relations</p>
                    <div className="mt-1 flex items-center gap-x-1.5">
                        <div className="flex-none rounded-full bg-emerald-500/20 p-1">
                        <div className="h-1.5 w-1.5 rounded-full bg-emerald-500"></div>
                        </div>
                        <p className="text-xs/5 text-gray-500">Online</p>
                    </div>
                    </div>
                </li>
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Lindsay Walton</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">lindsay.walton@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Front-end Developer</p>
                    <p className="mt-1 text-xs/5 text-gray-500">Last seen <time datetime="2023-01-23T13:23Z">3h ago</time></p>
                    </div>
                </li>
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Courtney Henry</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">courtney.henry@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Designer</p>
                    <p className="mt-1 text-xs/5 text-gray-500">Last seen <time datetime="2023-01-23T13:23Z">3h ago</time></p>
                    </div>
                </li>
                <li className="flex justify-between gap-x-6 py-5">
                    <div className="flex min-w-0 gap-x-4">
                    <div className="min-w-0 flex-auto">
                        <p className="text-sm/6 font-semibold text-gray-900">Tom Cook</p>
                        <p className="mt-1 truncate text-xs/5 text-gray-500">tom.cook@example.com</p>
                    </div>
                    </div>
                    <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p className="text-sm/6 text-gray-900">Director of Product</p>
                    <div className="mt-1 flex items-center gap-x-1.5">
                        <div className="flex-none rounded-full bg-emerald-500/20 p-1">
                        <div className="h-1.5 w-1.5 rounded-full bg-emerald-500"></div>
                        </div>
                        <p className="text-xs/5 text-gray-500">Online</p>
                    </div>
                    </div>
                </li>
                </ul>
        </main>
    );
}