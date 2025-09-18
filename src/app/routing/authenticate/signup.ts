'use server';

export async function addUser(formData: FormData){
    const rawFormData = {
        username: formData.get('username'),
        firstname: formData.get('firstname'),
        lastname: formData.get('lastname'),
        email: formData.get('email'),
        password: formData.get('password')   
    }
}