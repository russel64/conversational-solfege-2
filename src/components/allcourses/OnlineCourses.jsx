import React from "react"
import "./courses.css"
import { online } from "../../dummydata"
import Title from "../common/title/Title"
import { Link } from "react-router-dom/cjs/react-router-dom.min"


const OnlineCourses = () => {
  return (
    <>
      <section className='online'>
        <div className='container'>
          <Title subtitle='SAMPLE UNITS' title='View a Sample of Individual Units' />
          <div className='content grid3'>
            {online.map((val) => (
              <div className='box'>
                <div className='img'>
                  <img src={val.cover} alt=''/>
                  <img src={val.hoverCover} alt='' className='show' />
                </div>
                <h1>{val.courseName}</h1>
                <Link to='/assignments'>
                  <span>{val.course}</span>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}

export default OnlineCourses