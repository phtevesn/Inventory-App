'use server'

type loginForm = {
    usernameOrEmail: string, 
    password: string
}

export async function loginUser(loginData: loginForm){
    console.log(loginData)
    const res = await fetch("http://localhost:8000/users/login", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(loginData)
    });

    const status = res.status
    const result = await res.json();
    return {status, result};
}
