const videoElement = document.getElementById('video');
const startBtn = document.getElementById('startBtn');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    videoElement.srcObject = stream;
  })
  .catch(err => {
    console.error('Error accessing webcam: ', err);
  });

startBtn.addEventListener('click', () => {
  // Start the hand detection
  detectHand();
});

function detectHand() {
  // Here you would connect to the backend (Python) and get hand detection data
  canvas.style.display = 'block';
  ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
  // Call a WebSocket or HTTP API to send the canvas image to Python for processing
  console.log('Hand detection started');
}
