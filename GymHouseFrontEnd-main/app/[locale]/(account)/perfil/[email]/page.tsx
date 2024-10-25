'use client'

import { useParams } from 'next/navigation'
import React from 'react'



export default function page(){
    const {email} = useParams()
    console.log(email);
    
  return (
    <>
        <div>Perfil Usuario {email}</div>
    </>
  )
}

