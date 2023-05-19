import React, { useState } from 'react'

const defaultFormData = {
    title: '',
    image: '',
    unit: '',
    step: '',
    task: ''
  }

const AddAssignment = ({ handleAddAssignment }) => {
    const [formData, setFormData] = useState(defaultFormData)

    const handleChange = e => {
        setFormData({...formData, [e.target.name]: e.target.value})
    }

    const handleSubmit = e => {
        e.preventDefault()
        handleAddAssignment(formData)
        setFormData(defaultFormData)
    }


    return (
        <form onSubmit={ handleSubmit }>
            <div>
                <input onChange={handleChange} value={formData.title} type="text" name="title" placeholder="Title" />
                <input onChange={handleChange} value={formData.image} type="text" name="image" placeholder="Image URL" />
                <input onChange={handleChange} value={formData.unit} type="text" name="unit" placeholder="Unit" />
                <input onChange={handleChange} value={formData.step} type="text" name="step" placeholder="Step" />
                <input onChange={handleChange} value={formData.task} type="text" name="task" placeholder="Task" />
            </div>
            <input className="" type="submit" value="Add Assignment" />
        </form>
  )
}

export default AddAssignment