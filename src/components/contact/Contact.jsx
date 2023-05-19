import React, {useRef} from "react"
import Back from "../common/back/Back"
import "./contact.css"
import emailjs from '@emailjs/browser';

const Contact = () => {
  const form = useRef()

  const sendEmail = (e) => {
    e.preventDefault();

    emailjs.sendForm('service_emh9f4h', 'template_lknv9bj', form.current, 'UBmoNFjLd8cRkXU8O')
      .then((result) => {
          console.log(result.text);
      }, (error) => {
          console.log(error.text);
      });
      e.target.reset()
  };

  return (
    <>
      <Back title='Contact us' />
      <section className='contacts padding'>
        <div className='container shadow flexSB'>
          <div className='left row'>
            <img src='https://images.squarespace-cdn.com/content/v1/6196655ba0e926671f6f9cef/7f35b5fc-94c9-45b1-afb1-0a6ebd3eeb29/RiversideSchool_01_blurred.jpg?format=1500w' alt='' />
          </div>
          <div className='right row'>
            <h1>Contact Support Team</h1>
            <p>Have a question about a resource? Ask here!</p>

            <div className='items grid2'>
              <div className='box'>
                <h4>ADDRESS:</h4>
                <p>300 W 61st Street, New York New York 10023</p>
              </div>
              <div className='box'>
                <h4>EMAIL:</h4>
                <p> fake_name@schools.nyc.gov</p>
              </div>
              <div className='box'>
                <h4>PHONE:</h4>
                <p> +1 (123) 123 1234</p>
              </div>
            </div>

            <form ref={form} onSubmit={sendEmail} action=''>
              <div className='flexSB'>
                <input type='text' placeholder='Name' name='name'/>
                <input type='email' placeholder='Email' name='email'/>
              </div>
              <input type='text' placeholder='Subject' name='subject' />
              <textarea cols='30' rows='10' name='message' placeholder="Write your message here...">
              </textarea>
              <button className='primary-btn'>SEND MESSAGE</button>
            </form>
          </div>
        </div>
      </section>
    </>
  )
}

export default Contact