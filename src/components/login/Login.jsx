import React, { useState } from 'react'
import './login.css'
// import Back from '../common/back/Back'

const defaultFormData = {
  email: '',
  password: ''
}

const Login = (props) => {
  const [formData, setFormData] = useState('')

  const handleChange = e => {
    setFormData({...formData, [e.target.name]: e.target.value})
  }

  const handleSubmit = e => {
    e.preventDefault()
    console.log(formData)
    setFormData(defaultFormData)
  }

  return (
    <div className='auth-form-container'>
      {/* <Back /> */}
      <h2>Login</h2>
      <form className='login-form' onSubmit={handleSubmit}>
        <label for='email'>email</label>
        <input onChange={handleChange} value={formData.email} type="email" placeholder="email@gmail.com" id='email' name='email'/>
        <label for='password'>password</label>
        <input onChange={handleChange} value={formData.password} type="password" placeholder="*****" id='password' name='password'/>
        <button type="submit">Log In</button>
      </form>
      <button onClick={() => props.onFormSwitch('register')}>Don't have an account? Register Here!</button>
    </div>
  )
}

export default Login