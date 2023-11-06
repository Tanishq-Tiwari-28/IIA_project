import React from 'react'

import CompanyInfo from '../component/CompanyInfo'
import Partners from '../component/Partners'
import Hero from '../component/Hero'

const Home = () => {
  return (
    <div>
      <Hero />

      <CompanyInfo />

      <Partners />
    </div>
  )
}

export default Home