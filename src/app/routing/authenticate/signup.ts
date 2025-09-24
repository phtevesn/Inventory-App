'use server';

type signUpForm = {
    username: string,
    firstname: string, 
    lastname: string,
    email: string,
    password:string
}

export async function addUser(formData: signUpForm){

    const res = await fetch('http://localhost:8000/users/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
    });
    
    const result = await res.json();
    return result;
    
}