import { Header, Footer } from '@/components';


export default function HomeLayout({
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