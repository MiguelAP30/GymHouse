import { Header, Footer } from '@/components';
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Account",
  description: "Account is the section that only logged users can see"
};

export default function AccoutLayout({
 children
}: {
 children: React.ReactNode;
}) {
  return (
    <div>
      <Header />
      { children }
      <Footer />
    </div>
  );
}