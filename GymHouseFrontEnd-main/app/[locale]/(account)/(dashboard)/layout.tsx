'use client';
import React, { useEffect, useState } from 'react';

export default function DashboardLayout({
        children
    }: {
        children: React.ReactNode;
    }) {
    return (
        <div className="flex flex-col min-h-full">
            {children}
        </div>
    );
}