import React, {useState, useEffect} from "react"
import { Link } from "react-router-dom"
import "./footer.css"

const Footer = () => {
  const [blogs, setBlogs] = useState([])


  useEffect(() => {
    fetch('http://127.0.0.1:5555/blogs')
    .then(res => res.json())
    .then(data => setBlogs(data))
}, [])

  return (
    <>
      <footer>
        <div className='container padding'>
          <div className='box logo'>
            <h1>CS Online</h1>
            <span>Best Online Music Literacy Program</span>
            <p>Sound Before Sight Approach to become a tuneful, beaftul, artful person and lover of music! </p>

            <i className='fab fa-facebook-f icon' onClick={() => { window.open('https://www.facebook.com/groups/445107355586495', '_blank'); }}></i>
            <i className='fab fa-twitter icon' onClick={() => { window.open('https://twitter.com/feierabendmusic', '_blank'); }}></i>
            <i className='fab fa-youtube icon' onClick={() => { window.open('https://www.youtube.com/@feierabendassociationformu7684', '_blank'); }}></i>
          </div>
          <div className='box link'>
            <h3>Explore</h3>
            <ul>
              <li>
                <Link to='/about'>About</Link>
              </li>
              <li>
                <Link to='/courses'>All Courses</Link>
              </li>
              <li>
                <Link to='/assignments'>Samples</Link>
              </li>
              <li>
              <Link to='/bulletin'>Bulletin Board</Link>
              </li>
              <li>
              <Link to='/contact'>Contact</Link>
              </li>
            </ul>
          </div>
          <div className='box link'>
            <h3>Quick Links</h3>
            <ul>
              <li>Terms & Conditions</li>
              <li>Privacy</li>
              <li>Feedbacks</li>
            </ul>
          </div>
          <div className='box'>
            <h3>Recent Post</h3>
            {blogs.slice(0, 3).map((val) => (
              <div className='items flexSB'>
                <div className='img'>
                  <img src={val.cover} alt='' />
                </div>
                <div className='text'>
                  <span>
                    <i className='fa fa-calendar-alt'></i>
                    <label htmlFor=''>{val.date}</label>
                  </span>
                  <span>
                    <i className='fa fa-user'></i>
                    <label htmlFor=''>{val.author}</label>
                  </span>
                  <h4>{val.title.slice(0, 40)}...</h4>
                </div>
              </div>
            ))}
          </div>
          <div className='box last'>
            <h3>Have a Questions?</h3>
            <ul>
              <li>
                <i className='fa fa-map'></i>
                300 W 61st Street, New York New York 10023
              </li>
              <li>
                <i className='fa fa-phone-alt'></i>
                +1 (123) 123 1234
              </li>
              <li>
                <i className='fa fa-paper-plane'></i>
                fake_name@schools.nyc.gov
              </li>
            </ul>
          </div>
        </div>
      </footer>
      <div className='legal'>
        <p>
          {/* Copyright ©2022 All rights reserved | This template is made with <i className='fa fa-heart'></i> by GorkhCoder */}
        </p>
      </div>
    </>
  )
}

export default Footer