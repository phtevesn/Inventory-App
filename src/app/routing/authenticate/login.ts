'use server'

type loginForm = {
    username: string, 
    password: string
}

export async function loginUser(loginData: loginForm){

    const res = await fetch("http://localhost:8000/users/login", {
        method: 'POST',
        headers: {'Content-Type': 'application-json'},
        body: JSON.stringify(loginData)
    });

    const result = await res.json();
    return result;
}
