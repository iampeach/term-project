import React, { Component } from 'react'
import { Player } from 'video-react'

class Video extends Component {
  render() {
    return (
      <div className="capture">
        {(this.props.visible) &&
        <Display />}
      </div>
    )
  }
}

const Display = (props) => (
  <div className="camera">  
    <Player id="video" src="video/testfile.mp4"/>
  </div>
);

export default Video