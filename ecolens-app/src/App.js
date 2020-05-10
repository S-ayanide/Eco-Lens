import React, {useState, useEffect} from 'react';
import Dashboard from './view/Dashboard'
import './App.css';

function App() {

  // const [currentTime, setCurrentTime] = useState(0);

  // useEffect(() => {
  //   fetch('/time').then(res => res.json()).then(data => setCurrentTime(data.time))
  // }, [])

  return (
    <div className="App">      
      <Dashboard />
    </div>
  );
}

export default App;
