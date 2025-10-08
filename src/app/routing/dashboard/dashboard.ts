'use client'

export async function getUserStuff(){
  const res = await fetch("http://localhost:8000/users/me", {
    method: 'GET',
    credentials: 'include',
  });

  if (res.ok) {
    const test = await res.json();
    console.log(test)
    return test;
  } else {
    return "Failed to get stuff";
  }
}

export async function logout(){
  const res = await fetch("http://localhost:8000/users/logout", {
    method: 'POST',
    credentials: 'include',
  })

  const status = res.status;
  const result = await res.json();

  return {status, result};
}