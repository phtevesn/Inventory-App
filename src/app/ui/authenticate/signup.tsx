'use client';

import {useState} from 'react';
import Button from '@/app/utils/button'
import TextBox from '@/app/utils/auth-text';


export default function SignUp(){
    const[username, setUsername] = useState('');
    const[firstname, setFirstname] = useState('');
    const[lastname, setLastname] = useState('');
    const[email, setEmail] = useState('');
    const[password, setPassword] = useState('');
    const[confirmPassword, setConfirmPassword] = useState('');

    function submit(){
        alert(`username ${username} first ${firstname} last ${lastname} email ${email} 
            password ${password} confirm-pass ${confirmPassword}`);
    }

    return (
        <div>
            <form>
                <TextBox name='username' label='Username' type='text' value={username} onChange={setUsername} />
                <TextBox name='firstname' label='First Name' type='text' value={firstname} onChange={setFirstname} />
                <TextBox name='lastname' label='Last Name' type='text' value={lastname} onChange={setLastname} />
                <TextBox name='email' label='Email' type='text' value={email} onChange={setEmail} />
                <TextBox name='password' label='Password' type='password' value={password} onChange={setPassword} />
                <TextBox name='label' label='Confirm Password' type='password' value={confirmPassword} onChange={setConfirmPassword} />
                <button className="bg-slate-400 text-white px-4 py-2 rounded hover:bg-blue-400 transition-colors
                hover:scale-100 transition-all duration-200 ease-in-out active:scale-105 w-full mt-4" onClick={submit}
                > Verify Sign Up</button>
            </form>
        </div>
    );
}