import React from "react"

const Head = () => {
  return (
    <>
      <section className='head'>
        <div className='container flexSB'>
          <div className='logo'>
            <h1>Conversational Solfege Online</h1>
            {/* <span>Helping Everyone to Become Tuneful, Beatful, and Artful</span> */}
          </div>

          <div className='social'>
            <i className='fab fa-facebook-f icon' onClick={() => { window.open('https://www.facebook.com/groups/445107355586495', '_blank'); }}></i>
            <i className='fab fa-twitter icon' onClick={() => { window.open('https://twitter.com/feierabendmusic', '_blank'); }}></i>
            <i className='fab fa-youtube icon' onClick={() => { window.open('https://www.youtube.com/@feierabendassociationformu7684', '_blank'); }}></i>
          </div>
        </div>
      </section>
    </>
  )
}

export default Head



