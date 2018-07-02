import React, { Component } from 'react';
import "video-react/dist/video-react.css";
import './App.css';
import Capture from './Capture';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      videoStreaming: false
    }
  }
  createVideo = async () => {
    try {
      await fetch('/createVideo', {
        method: 'POST',
        headers: { Accept: "application/json" }
      })
    }
    catch(err) {
      console.log(err)
    }
  }
  receive = () => {
    this.setState({ videoStreaming: true })
  }
  render() {
    return (
      <div>
        <button onClick={this.createVideo}>Send</button>
        <button onClick={this.receive}>Receive</button>
        <Capture visible={this.state.videoStreaming} />
      </div>
    );
  }
}

export default App;
