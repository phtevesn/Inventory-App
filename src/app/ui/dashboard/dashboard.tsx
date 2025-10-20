'use client'

import {useState, useEffect} from 'react'
import {useRouter} from 'next/navigation';

import {getUserStuff} from "@/app/routing/dashboard/dashboard";
import {logoutUser} from "@/app/utils/users/logout"
import CreateInventory from "@/app/ui/inventory/create"

export default function Dashboard(){
  const router = useRouter();

  const [search, setSearch] = useState("");
  const [user, setUser] = useState<{ id: number; email: string } | null>(null);
  const [showForm, setShowForm] = useState(false);

  function createInv(){
    setShowForm(true);
  }

  useEffect(() => {
    async function loadUser() {
      const data = await getUserStuff();
      setUser(data)
    }

    loadUser();
  }, []);

  if (!user){
    return <div>Loading ma boi gimme a seccy</div>;
  }
  console.log(user.id)

  return (
    <div>
      <div><button onClick={logoutUser}> logout </button></div>
      <div className="flex flex-col justify-center items-center w-[500px] mt-40">
        <input
          className = "search-input"
          placeholder = "search your inventories"
          onChange = {(e)=> setSearch(e.target.value)}>
        </input>
        {!showForm && <button onClick={createInv} className="auth-button rounded-full mt-4"> create inventory </button>}
        {showForm && <CreateInventory />}
      </div>
    </div>
  );
}
