'use server';

type signUpForm = {
    username: string,
    firstname: string, 
    lastname: string,
    email: string,
    password:string
}

export async function addUser(formData: signUpForm){
    console.log(formData);

    /*
    const res = await fetch('http://localhost:5432', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
    });
    
   
    const result = await res.json();
    return result;
    */
}