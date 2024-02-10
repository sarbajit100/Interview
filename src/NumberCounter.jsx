import React from 'react'
import { useState } from 'react'

function NumberCounter() {
    const [number,setNumber] = useState(0)

  return (
    <div>
        <button onClick={()=> setNumber(number+1)}>Increase</button>
      <h1>{number}</h1>
      <button onClick={()=> setNumber(number-1)}>Decrease</button>
    </div>
  )
}

export default NumberCounter
