
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Auth",
  description: "Authentication section"
};

export default function AuthLayout({
 children
}: {
 children: React.ReactNode;
}) {
  return (
    <main className="w-full flex justify-between min-h-screen">
      <section></section>
      <section className="w-full flex justify-center items-center bg-[#011627]">
        {children}
      </section>
    </main>
  );
}