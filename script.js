// Access the webcam
const videoElement = document.getElementById('video');

// Start the video stream
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    videoElement.srcObject = stream;
  })
  .catch(err => {
    console.error("Error accessing the webcam: ", err);
  });
