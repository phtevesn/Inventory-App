'use client'

export async function logout(){
  const res = await fetch("http://localhost:8000/users/logout", {
    method: 'POST',
    credentials: 'include',
  })

  const status = res.status;
  const result = await res.json();

  return {status, result};
}