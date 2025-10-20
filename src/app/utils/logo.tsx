import Link from 'next/link';
import Image from 'next/image';


type LogoProps = {
  w: number;
  h: number; 
}
export default function Logo({w,h}: LogoProps){
  return(
    <Link href='/'>
      <Image src="/temp-logo.png" width={w} height={h} alt="Company Logo" />
    </Link>
  );
}