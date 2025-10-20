

import SignUp from '@/app/ui/authenticate/signup'
import Logo from '@/app/utils/logo'

export default function Page(){
    return (
        <div className="flex flex-col items-center justify-center min-h-screen pb-25">
            <Logo w={200} h={200}/>
            <h1>Inventory App</h1>
            <SignUp />
        </div>
    )
}