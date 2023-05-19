import React from 'react'
import Back from '../common/back/Back'
// import AssignmentsPage from './AssignmentsPage'



const AssignmentsHome = () => {
  return (
    <div>
      <Back title='Cnversational Solfege in Action' />
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
        }}
      >
        <div style={{ position: 'relative' }}>
          <img
            src="https://www.bethsnotesplus.com/wp-content/uploads/2014/07/Good-King-Wenceslas-1.png"
            alt="Good King Wenceslas"
            style={{ maxWidth: '100%', maxHeight: '100%', boxShadow: '0 0 10px rgba(0, 0, 0, 0.2)' }}
          />
          <button
            style={{
              position: 'absolute',
              top: '85%',
              left: '90%',
              transform: 'translate(-50%, -50%)',
              padding: '10px 20px',
              backgroundColor: '#fff',
              border: 'none',
              borderRadius: '4px',
              fontSize: '16px',
              fontWeight: 'bold',
              boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
              cursor: 'pointer',
            }}
            onClick={() => { window.open('https://www.youtube.com/watch?v=PynR9fZueUw', '_blank'); }}
          >
            Click to Watch
          </button>
        </div>
      </div>
    </div>
  );
};

export default AssignmentsHome


