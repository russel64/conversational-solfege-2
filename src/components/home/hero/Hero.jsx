import React from 'react'
import "./hero.css"
import Title from "../../common/title/Title"




const Hero = () => {
  return (
    <>
        <section className='hero'>
            <div className='container'>
                <div className='row'>
                    <Title subtitle='WELCOME TO CS ONLINE' title='The Best Music literacy Program' />
                    <h2>The sound before sight approach to helping students become tuneful, beatful, and artful!</h2>
                </div>
            </div>
        </section>
        <div className='margin'></div>
    </>
  )
}

export default Hero