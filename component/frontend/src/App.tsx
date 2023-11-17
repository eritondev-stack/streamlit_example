import React, { useEffect, useState } from 'react';
import './App.css';
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib"

const Component = ({ args }: ComponentProps) => {
  const [count, setCount] = useState(0)
  useEffect(() => Streamlit.setFrameHeight())

  const handleClick = () => {
    var count2 = count + 1
    setCount(count2)
    Streamlit.setComponentValue({
      count: count2
    })
  }
  return (
    <div>
      <div className="text-red-500">{args.spec}</div>
      <button onClick={handleClick}>Count: {count}</button>
      <h1 className="text-3xl font-bold underline bg-green-300">
        Hello world!
      </h1>
    </div>
  )
}

export default withStreamlitConnection(Component)