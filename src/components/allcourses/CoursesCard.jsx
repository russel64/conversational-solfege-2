import React, {useState, useEffect} from "react"
import "./courses.css"
// import { coursesCard } from "../../dummydata"

const CoursesCard = () => {
  const [courses, setCourses] = useState([])


  useEffect(() => {
    fetch('http://127.0.0.1:5555/courses')
    .then(res => res.json())
    .then(data => setCourses(data))
}, [])

  return (
    <>
      <section className='coursesCard'>
        <div className='container grid2'>
          {courses.map((val) => (
            <div className='items'>
              <div className='content flex'>
                <div className='left'>
                  <div className='img'>
                    <img src={val.cover} alt='' />
                  </div>
                </div>
                <div className='text'>
                  <h1>{val.coursesName}</h1>
                  <div className='rate'>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <i className='fa fa-star'></i>
                    <label htmlFor=''>(5.0)</label>
                  </div>
                  <div className='details'>
                    {val.courTeachers.map((details) => (
                      <>
                        <div className='box'>
                          <div className='dimg'>
                            <img src={details.dcover} alt='' />
                          </div>
                          <div className='para'>
                            <h4>{details.name}</h4>
                          </div>
                        </div>
                        <span>{details.totalTime}</span>
                      </>
                    ))}
                  </div>
                </div>
              </div>
              <div className='price'>
                <h3>
                  {val.priceAll} / {val.pricePer}
                </h3>
              </div>
              <button className="outline-btn" onClick={() => { window.open('https://www.giamusic.com/store/search?giaSession=me&elSearchTerm=conversational+solfege&elCatalog%5B%5D=me', '_blank'); }}>ENROLL NOW!</button>

            </div>
          ))}
        </div>
      </section>
    </>
  )
}

export default CoursesCard


