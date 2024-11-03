import { Header, Footer } from '../../../components';


export default function HomeLayout({
 children
}: {
 children: React.ReactNode;
}) {
  return (
    <div className="h-screen flex flex-col">
      <Header />
      <div className="flex-grow">
        {children}
      </div>
      <Footer />
    </div>
  );
}