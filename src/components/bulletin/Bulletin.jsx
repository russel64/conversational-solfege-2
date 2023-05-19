import React from 'react'
import BulletinCard from './BulletinCard'
import Back from '../common/back/Back'
import "./bulletin.css"


const Bulletin = () => {
    return (
        <>
          <Back title='Bulletin Board' />
          <section className='bulletin padding'>
            <div className='container grid2'>
              <BulletinCard />
            </div>
          </section>
        </>
      )
    }

export default Bulletin