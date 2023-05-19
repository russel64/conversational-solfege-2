import React from 'react'
import Hero from "./hero/Hero"
import AboutCard from '../about/AboutCard'
import HAbout from './HAbout'
import Test from './testimonial/Test'



const Home = () => {
  return (
    <>
        <Hero />
        <AboutCard/>
        <HAbout />
        <Test />
    </>
  )
}

export default Home