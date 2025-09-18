import Image from "next/image";
import '@/app/globals.css';

import LoginButton from '@/app/utils/login';
import SignUpButton from "@/app/utils/signup";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1>Inventory App</h1>
      <p>Modular Adaptible Inventory System</p>
      <div className="flex mt-4 space-x-10">
        <LoginButton />
        <SignUpButton />
      </div>
      
    </div>
  );
}
