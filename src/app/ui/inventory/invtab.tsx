'use client'

import Link from "next/link";

type InvTabProps = {
    invID : number;
    invName : string;
}
export default function InvTab({ invID, invName }: InvTabProps){
    return (
        <div>
            <Link href ={`/inventory/${invID}`}>
                <div className="inv-tab hover:bg-slate-300 transition-colors
                hover:scale-100 transition-all duration-200 ease-in-out active:scale-105">
                    {invName}
                </div>
            </Link>
        </div>
    );
}