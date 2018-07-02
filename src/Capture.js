import React, { Component } from 'react'
import { Player } from 'video-react'
import FormData from 'form-data'

class Capture extends Component {
  constructor(props) {
    super(props)

    this.state = {
      constraints: { audio: true, video: { width: 400, height: 300 } },
      isInitialed: false
    }

    // this.handleStartClick = this.handleStartClick.bind(this)
    // this.takePicture = this.takePicture.bind(this)
    // this.clearPhoto = this.clearPhoto.bind(this)
  }
  componentDidMount = async () => {
    // const constraints = this.state.constraints
    // navigator.getUserMedia = navigator.getUserMedia ||
    //                          navigator.webkitGetUserMedia ||
    //                          navigator.mozGetUserMedia;
    // const getUserMedia = params => (
    //   new Promise((successCallback, errorCallback) => {
    //     navigator.getUserMedia.call(navigator, params, successCallback, errorCallback)
    //   })
    // )

    // this.clearPhoto()

    try {
    //   const stream = await getUserMedia(constraints)
    //   const video = document.querySelector('video')
    //   const vendorURL = window.URL || window.webkitURL
    //   const blob = vendorURL.createObjectURL(stream)

    //   var fd = new FormData()
    //   fd.append('name', blob)
      await fetch('/createVideo', {
        method: 'POST',
        headers: { Accept: "application/json" }
      })
      this.setState({ isInitialed: true })
    //   var src = await fetch('/video/testfile.mp4')
    //   console.log(src)
    //   video.src = src
    //   video.play()
    }
    catch(err) {
      console.log(err)
    }
  }
  clearPhoto () {
    const canvas = document.querySelector('canvas');
    const photo = document.getElementById('photo');
    const context = canvas.getContext('2d');
    const { width, height } = this.state.constraints.video;
    context.fillStyle = '#FFF';
    context.fillRect(0, 0, width, height);

    const data = canvas.toDataURL('image/png');
    photo.setAttribute('src', data);
  }
  handleStartClick(event) {
    event.preventDefault();
    this.takePicture();
  }
  takePicture() {
    const canvas = document.querySelector('canvas');
    const context = canvas.getContext('2d');
    const video = document.querySelector('video');
    const photo = document.getElementById('photo');
    const { width, height } = this.state.constraints.video;

    canvas.width = width;
    canvas.height = height;
    context.drawImage(video, 0, 0, width, height);

    const data = canvas.toDataURL('image/png');
    photo.setAttribute('src', data);
  }
  render() {
    return (
      <div className="capture">
        {(this.state.isInitialed) &&
        <Camera />}
      </div>
    )
  }
}

const Camera = (props) => (
  <div className="camera">  
    <Player id="video" src="video/testfile.mp4"/>
  </div>
);

const Photo = (props) => (
  <div className="output">
    <img id="photo" alt="Your photo" />
    <a id="saveButton"
      onClick={ props.handleSaveClick }
    >Save Photo</a>
  </div>
);

export default Capture