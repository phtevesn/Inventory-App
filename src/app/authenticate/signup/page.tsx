import Link from 'next/link';
import Image from 'next/image';

import SignUp from '@/app/ui/authenticate/signup'

export default function Page(){
    return (
        <div className="flex flex-col items-center justify-center min-h-screen pb-25">
            <Link href='/'>
                <Image src="/temp-logo.png" width={200} height={200} alt="Company Logo" />
            </Link>
            <h1>Inventory App</h1>
            <SignUp />
        </div>
    )
}