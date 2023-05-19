import React from 'react'

const Assignment = ({ assignment }) => {

    const {id, title, image, unit, step, task} = assignment
  
  
    return (
        <tr className="table-row">
            <td className="row-image">
                <img src={image} alt="title" />
            </td>
            <td className="row-title">{title}</td>
            <td>{unit}</td>
            <td>{step}</td>
            <td>{task}</td>
            <td><button >Delete</button></td>
        </tr>
  )
}

export default Assignment