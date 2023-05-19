import React from 'react'
import Assignment from './Assignment'

const AssignmentList = ({ assignments }) => {
  return (
    <table>
      <tbody>
        <tr>
          <th>
          <h3 className="row-image">Img</h3>

          </th>
          <th>
            <h3 className="row-title">Title</h3>
          </th>
          <th>
            <h3 className="unit">Unit</h3>
          </th>
          <th>
            <h3 className="step">Step</h3>
          </th>
          <th>
            <h3 className="task">Task</h3>
          </th>
        </tr>
        {assignments.map(assignment => <Assignment key={assignment.id} assignment={assignment} />)}
      </tbody>
    </table>
  )
}

export default AssignmentList