'use client'
import { CardRutina } from '@/components/organisms/CardRutina'
import { useParams } from 'next/navigation'
import React from 'react'

export default function page(){

    const {id} = useParams()
  return (
    <>
    <CardRutina idCard={`${id}`} />
    <div>page  </div>
    </>
  )
}
