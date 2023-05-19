import React, {useState, useEffect} from "react"
// import { blog } from "../../dummydata"

const BulletinCard = () => {
  const [blogs, setBlogs] = useState([])


  useEffect(() => {
    fetch('http://127.0.0.1:5555/blogs')
    .then(res => res.json())
    .then(data => setBlogs(data))
}, [])




  return (
    <>
      {blogs.map((val) => (
        <div className='items shadow'>
          <div className='img'>
            <img src={val.cover} alt='' />
          </div>
          <div className='text'>
            <div className='admin flexSB'>
              <span>
                <i className='fa fa-user'></i>
                <label htmlFor=''>{val.author}</label>
              </span>
              <span>
                <i className='fa fa-calendar-alt'></i>
                <label htmlFor=''>{val.date}</label>
              </span>
              <span>
                <i className='fa fa-comments'></i>
                <label htmlFor=''>{val.com}</label>
              </span>
            </div>
            <h1>{val.title}</h1>
            <p>{val.desc}</p>
          </div>
        </div>
      ))}
    </>
  )
}

export default BulletinCard