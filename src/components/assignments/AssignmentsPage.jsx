import React, {useEffect, useState} from 'react'
import AssignmentList from './AssignmentList'
import AddAssignment from './AddAssignment'
import './assignments.css'

const AssignmentsPage = () => {
    const [assignments, setAssignments] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:5555/assignments')
        .then(res => res.json())
        .then(data => setAssignments(data))
    }, [])


    const handleAddAssignment = newAssignment => {
    fetch('http://127.0.0.1:5555/assignments', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newAssignment)
    })
    .then(res => res.json())
    .then(data => setAssignments([...assignments, data]))
}




  return (
    <div>
        <AddAssignment handleAddAssignment={handleAddAssignment} />
        <AssignmentList assignments={assignments}/>
    </div>
  )
}

export default AssignmentsPage