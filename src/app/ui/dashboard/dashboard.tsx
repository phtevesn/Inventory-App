'use client'

import {useState, useEffect} from 'react'
import {useRouter} from 'next/navigation';

import {getUserStuff} from "@/app/routing/dashboard/dashboard";
import {logoutUser} from "@/app/utils/users/logout"
import CreateInventory from "@/app/ui/inventory/create"
import InvTab from '@/app/ui/inventory/invtab';

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
  

  const sampo_data = [  //temp data
    { invID: 1, invName: "Groceries" },
    { invID: 2, invName: "Electronics" },
    { invID: 3, invName: "Clothes" },
    { invID: 4, invName: "Books" },
    { invID: 5, invName: "Furniture" },
  ];


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
        <div className="flex flex-col justify-center items-center mt-10 space-y-4">
          {sampo_data.map((inv) => (
            <div key={inv.invID}>
              <InvTab invID={inv.invID} invName={inv.invName} />
            </div>
          ))}
        </div>
    </div>
  );
}
