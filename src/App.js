import React, { Component } from 'react';
import Webcam from 'react-webcam';
import './App.css';
import Capture from './Capture';

class App extends Component {
  render() {
    return (
      <div>
        <Capture />
      </div>
    );
  }
}

export default App;
