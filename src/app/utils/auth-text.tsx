'use client'

import {useState} from 'react'

type TextBoxProps = {
  name: string;
  label: string;
  type: string;
  value: string;
  onChange: (val: string) => void;
};

export default function TextBox({name, label, type, value, onChange}: TextBoxProps){

    return (
        <div>
            <p>{label}:</p>
            <input
                name={name}
                className='form-input'
                type={type}
                value={value}
                onChange={(e) => onChange(e.target.value)}
            />
        </div>
    );
}
