'use client';

import {useState} from 'react';
import Button from '@/app/utils/button'
import TextBox from '@/app/utils/auth-text';
import {addUser} from '@/app/routing/authenticate/signup'

export default function SignUp(){
    const[username, setUsername] = useState('');
    const[firstname, setFirstname] = useState('');
    const[lastname, setLastname] = useState('');
    const[email, setEmail] = useState('');
    const[password, setPassword] = useState('');
    const[confirmPassword, setConfirmPassword] = useState('');
    const[passMessage, setPassMessage] = useState('')
    const badMessage = "when it says confirm password usually you put the same password"
    const goodMessage = "good job at typing"

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault(); 
        const formData = {
            username,
            firstname,
            lastname,
            email,
            password
        };
        if (password !== confirmPassword) {
            setPassMessage(badMessage);
        } else {
            setPassMessage(goodMessage);
            await addUser(formData)
        }
        
    };

    return (
        <div className="w-[300px]">
            <form onSubmit={handleSubmit}>
                <TextBox name='username' label='Username' type='text' value={username} onChange={setUsername} required/>
                <TextBox name='firstname' label='First Name' type='text' value={firstname} onChange={setFirstname} required/>
                <TextBox name='lastname' label='Last Name' type='text' value={lastname} onChange={setLastname} required />
                <TextBox name='email' label='Email' type='text' value={email} onChange={setEmail} required />
                <TextBox name='password' label='Password' type='password' value={password} onChange={setPassword} required/>
                <TextBox name='confirmPassword' label='Confirm Password' type='password' value={confirmPassword} onChange={setConfirmPassword} required/>
                <p
                className={`w-full text-center ${
                    passMessage.includes(badMessage) ? "text-red-500" : "text-green-500"
                }`}
                >{passMessage}</p>
                <button type='submit' className="auth-button w-full mt-4"> Verify Sign Up</button>
            </form>
        </div>
    );
}