import React, { useState } from 'react'
import axios from 'axios'

const defaultFormData = {
  email: '',
  password: ''
  // name: ''
}

const Register = (props) => {
  const [formData, setFormData] = useState('')
  const [users, setUsers] = useState([])

  const handleAddUsers = newUser => {
    fetch('http://127.0.0.1:5555/users', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newUser)
    })
    .then(res => res.json())
    .then(data => setUsers([...users, data]))
}

  const handleChange = e => {
    setFormData({...formData, [e.target.name]: e.target.value})
  }

  const handleSubmit = e => {
    e.preventDefault()
    handleAddUsers(formData)
    console.log(formData)
    setFormData(defaultFormData)
  }

  return (
    <div className='auth-form-container'>
      <h2>Register</h2>
      <form className='register-form' onSubmit={handleSubmit}>
        {/* <label for='name'>Full Name</label>
        <input onChange={handleChange} value={formData.name} name="name" id="name" placeholder="Full Name" /> */}
        <label for='email'>email</label>
        <input onChange={handleChange} value={formData.email} type="email" placeholder="email@gmail.com" id='email' name='email'/>
        <label for='password'>password</label>
        <input onChange={handleChange} value={formData.password} type="password" placeholder="*****" id='password' name='password'/>
        <button type="submit">Register</button>
      </form>
      <button onClick={() => props.onFormSwitch('login')}>Already have an account? Log in here!</button>
    </div>
  )
}

export default Register