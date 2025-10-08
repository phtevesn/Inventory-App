'use client'

type loginForm = {
    usernameOrEmail: string, 
    password: string
}

export async function loginUser(loginData: loginForm){
    console.log(loginData)

     const body = new URLSearchParams({
        username: loginData.usernameOrEmail, 
        password: loginData.password,
    });
    const res = await fetch("http://localhost:8000/users/login", {
        method: 'POST',
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body,
        credentials: "include"
    });

    const status = res.status
    const result = await res.json();
    return {status, result};
}
