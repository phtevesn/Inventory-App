
import {redirect} from 'next/navigation'

import {logout} from '@/app/routing/authenticate/logout'

export async function logoutUser(){

  const response = await logout();
  if (response.status === 200){
    redirect('/')
  }
}