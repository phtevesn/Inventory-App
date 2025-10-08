'use client';

import {useState} from 'react';
import {useRouter} from 'next/navigation';

import SignUpButton from '@/app/utils/signup'
import TextBox from '@/app/utils/auth-text';
import { loginUser } from '@/app/routing/authenticate/login';


export default function Login(){
    const [usernameOrEmail, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const router = useRouter();
    const invalidMessage = "your credentials are wrong gangy"


    const submitAuth = async (e: React.FormEvent) => {
        e.preventDefault();
        const formData = {
            usernameOrEmail, password
        }
        try {
            const response = await(loginUser(formData))
            if (response.status ===200){
                console.log(response);
                router.push('/dashboard');
            } 
            else if (response.status === 401) setMessage(invalidMessage)
        } catch (error) {
            console.log("no gang");
        }
    }

    return (
    <div className="space-y-2 w-[300px]">
        <form onSubmit={submitAuth}>
            <TextBox name='username' label="username/email" type='text' value={usernameOrEmail} onChange={setUsername} required/>
            <TextBox name='password' label="password" type='password' value={password} onChange={setPassword} required/>
            <p className="w-full text-center text-red-400" > {message} </p>
            <div className="flex mt-4 ">
                <SignUpButton />
                <button type='submit' className='auth-button ml-auto'>Login</button>
                
            </div>
        </form>
    </div>);
}