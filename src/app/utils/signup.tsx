  
  
'use client';

import { useRouter } from 'next/navigation';
import Button from '@/app/utils/button'

export default function SignUpButton() {
    const router = useRouter();

    function signUp() {
        console.log("You're tickling me!");
        router.push('/authenticate/signup');
    }

    return (
        <Button buttonName="Sign-Up" onClick={signUp} />
    );
}