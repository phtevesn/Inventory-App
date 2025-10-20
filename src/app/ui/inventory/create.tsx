'use client'

import {useState} from 'react'

export default function CreateInventory(){
  const [invName, setInvName] = useState('');

  const submitAuth = async (e: React.FormEvent) => {
    e.preventDefault();
    
  }

  return (
    <div className="flex">
      <form onSubmit={submitAuth}>
        <input 
          className = "bg-blue-200 text-gray-900 rounded-full pr-4 pl-4"
          onChange = {(e)=> setInvName(e.target.value)}
          placeholder = "inventory name">
        </input>
        <button type="submit" className="auth-button rounded-full ml-1 mt-4 px-2 py-0">+</button>
      </form>

      <div>
        {/* here is where i get my inventories */}
      </div>
    </div>
  );
}