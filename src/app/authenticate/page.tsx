

import Login from '@/app/ui/authenticate/login'
import Logo from '@/app/utils/logo'

export default function AuthPage(){
    return (
    <div className="flex flex-col items-center justify-center min-h-screen pb-30">
        <Logo w={200} h={200}/>
        <h1>Inventory App</h1>
        <Login />
    </div> );
}

