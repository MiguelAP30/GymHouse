'use client';
import Image from 'next/image';
import Link from 'next/link';
import { MarkGithubIcon } from '@primer/octicons-react';
import { hoverscale, hoverLink } from '../tokens';

export const Footer = () => {
    return (
        <footer className="w-full max-w-full h-[140] max-h-full bg-[#17455A] flex justify-between items-center">
            <aside className="ml-[40px] mr-[100px] flex ">
                <ul className="flex flex-col ml-0 mr-1">
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}` }
                        href="https://www.instagram.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_instagram.png'
                            alt="logo instagram" 
                            width={50}
                            height={50}
                            />
                        @GymHouse
                    </Link>
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}` }
                        href="https://www.youtube.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_youtube.png'
                            alt="logo youtube" 
                            width={50}
                            height={50}
                            />
                        GymHouseYT
                    </Link>
                    <Link className={`flex flex-row items-center justify-start ${hoverLink} ${hoverscale}` }
                        href="https://www.twitter.com">
                        <Image 
                            className={`w-[25px] h-[25px] mr-2.5 ${hoverscale}`}
                            src='/logo_twitter.png'
                            alt="logo twitter" 
                            width={50}
                            height={50}
                            />
                        @GymHouse
                    </Link>
                </ul>
            </aside>
            <section className="flex flex-col mr-5">
                <ul className="w-[100px] h-[100px]">
                    <Link className={`flex flex-row items-center justify-center ${hoverLink} ${hoverscale}`}
                        href="https://github.com/MiguelAP30">
                            <MarkGithubIcon size={80} />
                    </Link>
                </ul>
            </section>
        </footer>
    )
}