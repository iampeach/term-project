import React, { Component } from 'react';
import "video-react/dist/video-react.css";
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
