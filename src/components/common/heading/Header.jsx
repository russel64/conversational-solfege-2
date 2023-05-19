import React, { useState } from "react"
import { Link } from "react-router-dom"
import Head from "./Head"
import "./header.css"

const Header = () => {
  const [click, setClick] = useState(false)

  return (
    <>
      <Head />
      <header>
        <nav className='flexSB'>
          <ul className={click ? "mobile-nav" : "flexSB "} onClick={() => setClick(false)}>
            <li>
              <Link to='/'>Home</Link>
            </li>
            <li>
              <Link to='/about'>About</Link>
            </li>
            <li>
              <Link to='/courses'>All Courses</Link>
            </li>
            <li>
              <Link to='/assignments'>Samples</Link>
            </li>
            {/* <li>
              <Link to='/team'>Specialists</Link>
            </li> */}
            <li>
              <Link to='/bulletin'>Bulletin Board</Link>
            </li>
            <li>
              <Link to='/contact'>Contact</Link>
            </li>
          </ul>
          <div className='start'>
            <div className='button' onClick={() => { window.open('https://harttsummerterm.hartford.edu/hartt/summerterm/registration/course-detail.aspx?c=36', '_blank'); }}>Summer Certification Here
              {/* <Link to='/login'>Login/Register</Link> */}
            </div>
          </div>
          <button className='toggle' onClick={() => setClick(!click)}>
            {click ? <i className='fa fa-times'> </i> : <i className='fa fa-bars'></i>}
          </button>
        </nav>
      </header>
    </>
  )
}

export default Header