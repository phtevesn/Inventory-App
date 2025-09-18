'use client';

type ButtonProps = {
  buttonName: React.ReactNode;
  onClick: () => void;
};

export default function Button({ buttonName, onClick}: ButtonProps){

    return (
        <button className="bg-slate-400 text-white px-4 py-2 rounded hover:bg-blue-400 transition-colors
        hover:scale-100 transition-all duration-200 ease-in-out active:scale-105" onClick={onClick}
        > {buttonName} </button>
    );
}
