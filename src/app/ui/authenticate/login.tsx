'use client';

import {useState} from 'react';
import Button from '@/app/utils/button'
import SignUpButton from '@/app/utils/signup'
import TextBox from '@/app/utils/auth-text';


export default function Login(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    function submitAuth(){
        alert(`Username ${username} Password ${password}`);
    }

    return (
    <div className="space-y-2">
        <TextBox name='username' label="username/email" type='text' value={username} onChange={setUsername} />
        <TextBox name='password' label="password" type='password' value={password} onChange={setPassword} />

        <div className="flex mt-4 space-x-10">
            <Button buttonName="Login" onClick={submitAuth} />
            <SignUpButton />
        </div>
    </div>);
}