import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { metadataHome } from "@/components/metadata";


const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = metadataHome;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
