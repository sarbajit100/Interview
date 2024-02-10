import React, { useState } from 'react'
import img1 from '../public/(1).jpg'
import img2 from '../public/(2).jpg'
import img3 from '../public/(3).jpg'
import img4 from '../public/(4).jpg'
import img5 from '../public/(5).jpg'
import img6 from '../public/(6).jpg'
const Image_data = [
    img1,
    img2,
    img3,
    img4,
    img5,
    img6
    
]
function ImageSlider() {
    const[img, setImg] = useState(0)
    function next() {
        if (img == 5) {
            setImg(img-img)
        } else {
            setImg(img+1)  
        }
        
    }
    function prev() {
        if (img == 0) {
            setImg(Image_data.length-1)
        } else {
            setImg(img-1)  
        }
    }
    
  return (
    <div style={{display:"flex", alignItems:"center", justifyContent:"center"}}>
        <button onClick={prev}>Prev</button>
      <img src={Image_data[img]} alt="" style={{height:"500px", width:"500"}}/>
      <button onClick={next}>Next</button>
    </div>
  )
}

export default ImageSlider
