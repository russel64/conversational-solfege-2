import React from "react"
import "./about.css"
import { homeAbout } from "../../dummydata"
import AWrapper from "./AWrapper"
import Title from "../common/title/Title"


const AboutCard = () => {
  return (
    <>
      <section className='aboutHome'>
        <div className='container flexSB'>
          <div className='left row'>
            <img src='https://pbs.twimg.com/media/DoxCHwoXsAEbin4?format=jpg&name=large' alt='' />
          </div>
          <div className='right row'>
            <Title subtitle='Master Music Literacy' title='Benefits of Conversational Solfege Curriculum' />
            <div className='items'>
              {homeAbout.map((val) => {
                return (
                  <div className='item flexSB'>
                    <div className='img'>
                      <img src={val.cover} alt='' />
                    </div>
                    <div className='text'>
                      <h2>{val.title}</h2>
                      <p>{val.desc}</p>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        </div>
      </section>
      <AWrapper />
    </>
  )
}

export default AboutCard