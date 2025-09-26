'use client';

import {useState} from 'react';
import Link from 'next/link';

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
    const[passMessage, setPassMessage] = useState('');
    const[login, setLogin] = useState('go to login');
    const badMessage = "when it says confirm password usually you put the same password";
    const goodMessage = "good job at typing you're in";
    const whatMessage = "what the hecky it didn't go through hmm";
    const loginMess = "GO TO LOGIN!";
    const userConflict = "uh oh someone has this username L";
    const emailConflict = "ermmm this email is already registerd";
    const [submitSuccess, setSubmitSuccess] = useState(false);


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
            const response = await addUser(formData)
            if (response.status === 200) {
                setPassMessage(goodMessage);
                setSubmitSuccess(true);
                setLogin(loginMess);
                resetForm();
            } else {
                if (response.result.detail === "user") setPassMessage(userConflict);
                else if (response.result.detail === "email") setPassMessage(emailConflict);
                else setPassMessage(whatMessage);
            }
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
                <p className={`w-full text-center ${passMessage.includes(goodMessage) ? "text-green-400" : "text-red-400"}`}>
                    {passMessage}
                </p>
                <button type='submit' className="auth-button w-full mt-2"> Complete Sign Up</button>
                <div className="flex justify-center">
                    <div className={`inline-flex mt-3 p-1 ${submitSuccess ? "border border-green-400 rounded-md" : ""} `}>
                        <Link href='/authenticate' className="text-center">{login}</Link>
                    </div>
                </div>
                
            </form>
        </div>
    );

    function resetForm() {
        setUsername("");
        setFirstname("");
        setLastname("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
    }
}


