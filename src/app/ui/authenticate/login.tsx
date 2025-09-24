'use client';

import {useState} from 'react';
import Button from '@/app/utils/button'
import SignUpButton from '@/app/utils/signup'
import TextBox from '@/app/utils/auth-text';

import { loginUser } from '@/app/routing/authenticate/login';


export default function Login(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    const submitAuth = async (e: React.FormEvent) => {
        e.preventDefault();
        const formData = {
            username, password
        }
        try {
            const response = await(loginUser(formData))
            console.log("gang");
        } catch (error) {
            console.log("no gang");
        }
        
    }

    return (
    <div className="space-y-2">
        <form onSubmit={submitAuth}>
            <TextBox name='username' label="username/email" type='text' value={username} onChange={setUsername} />
            <TextBox name='password' label="password" type='password' value={password} onChange={setPassword} />

            <div className="flex mt-4 space-x-10">

                <button type='submit' className='auth-button'>Login</button>
                <SignUpButton />
            </div>
        </form>
    </div>);
}