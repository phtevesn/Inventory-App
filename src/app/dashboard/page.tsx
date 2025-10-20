

import Dashboard from '@/app/ui/dashboard/dashboard';
import Logo from '@/app/utils/logo'

export default function Page(){
  return (
    <div>
      <div className="ml-4 mt-2">
        <Logo w={40} h={40}/>
      </div>
      <div className = "flex justify-center">
        <Dashboard />
      </div>
    </div>
  )
}