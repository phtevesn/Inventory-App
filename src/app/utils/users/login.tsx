'use client';

import { useRouter } from 'next/navigation';
import Button from '@/app/utils/button'

export default function LoginButton() {
  const router = useRouter();

  function login() {
    console.log("You're touching me!");
    router.push('/authenticate');
  }
  return (
    <div>
      <Button buttonName="Login" onClick={login} />
    </div>
  );
}
