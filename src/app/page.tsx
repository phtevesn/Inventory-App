import Image from "next/image";
import LoginButton from '@/app/ui/button';


export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1>Inventory App</h1>
      <div className="flex">
        <LoginButton />
      </div>
      
    </div>
  );
}
