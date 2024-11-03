import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { metadataHome } from "../../components/metadata";
import { NextIntlClientProvider } from 'next-intl'; 
import { getMessages } from "next-intl/server";


const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = metadataHome;

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const messages = await getMessages();
  return (
    <NextIntlClientProvider messages= {messages}> 
      <html lang="en" className="h-full"> 
          <body className={`${inter.className}h-full flex flex-col `}>
              {children}
          </body>
      </html>
    </NextIntlClientProvider>
  );
}
