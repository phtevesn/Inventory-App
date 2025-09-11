'use client';

export default function LoginButton(){
    function touchingMe(){
        console.log("Youre touching me")
    }

    return (
        <button className="bg-slate-400 text-white px-4 py-2 rounded hover:bg-cyan-500 transition-colors
        hover:scale-100 transition-all duration-200 ease-in-out" onClick={touchingMe}> Login </button>
    );
}