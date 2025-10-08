'use client'

import {useState, useEffect} from 'react'
import {useRouter} from 'next/navigation';

import { getUserStuff, logout } from "@/app/routing/dashboard/dashboard";

export default function Dashboard(){
    const router = useRouter();

    const [user, setUser] = useState<{ id: number; email: string } | null>(null); //why does this need to be set to null 
    async function logoutUser(){
        const response = await logout();
        if (response.status === 200){
            router.push("/");
        }
    }

    useEffect(() => {
        async function loadUser() {
            const data = await getUserStuff();
            setUser(data)
        }

        loadUser();
    }, []);

    if (!user) return <div>Loading ma boi gimme a seccy</div>;

    return (
        <div className="flex justify-center  mt-4">
            <p className = "border border-neutral-200">
                penis {user.id}
            </p>
            <button onClick={logoutUser}> logout </button>
            
        </div>
    );
}
