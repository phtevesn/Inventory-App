'use client'

import {useState} from 'react'

type TextBoxProps = {
  name: string;
  label: string;
  type: string;
  value: string;
  onChange: (val: string) => void;
  required?: boolean;
};

export default function TextBox({name, label, type, value, onChange, required}: TextBoxProps){

    return (
        <div>
            <p>{label}:</p>
            <input
                name={name}
                className='form-input'
                type={type}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                required={required}
            />
        </div>
    );
}
