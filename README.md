# Hand Detector

This project implements a **Hand Detector** using the [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/hands) library. It detects and visualizes hand landmarks in real-time using a webcam feed.

## Features

- **Real-Time Hand Detection**: Detects up to two hands and identifies 21 landmarks per hand.
- **Canvas Rendering**: Displays the webcam feed with landmarks overlaid in real time.
- **Customizable Visualization**: Easily modify the rendering style (e.g., colors, sizes, or connections).

## Installation

To use this project, simply include the following dependencies in your HTML file:

```html
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js"></script>
```

## How It Works

1. **Video Input**:
   - The `video` element captures a live feed from the user's webcam.

2. **Hand Detection**:
   - The MediaPipe Hands model processes the video frames to detect hand landmarks.

3. **Canvas Output**:
   - The detected landmarks are drawn on a `canvas` element over the video frame.

4. **Camera Integration**:
   - The MediaPipe `Camera` utility handles webcam access and streams frames to the hand detection model.

## Usage

1. Clone or download this repository.
2. Open the `index.html` file in a browser that supports MediaPipe (e.g., Chrome).
3. Allow camera access when prompted.
4. Observe the hand landmarks overlaid on the video feed in real-time.

## Code Overview

### HTML Structure

- **Video Input**: Captures the webcam feed.
- **Canvas Output**: Displays the processed video frames with hand landmarks.

### JavaScript Logic

- Initialize the MediaPipe Hands model:
  ```javascript
  const hands = new Hands({
      locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
  });
  hands.setOptions({
      maxNumHands: 2,
      modelComplexity: 1,
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5
  });
  ```
- Configure the `Camera` object:
  ```javascript
  const camera = new Camera(video, {
      onFrame: async () => {
          await hands.send({ image: video });
      },
      width: 840,
      height: 680
  });
  camera.start();
  ```
- Draw landmarks on the canvas:
  ```javascript
  hands.onResults(results => {
      // Draw landmarks here
  });
  ```

## Customization

- **Landmark Styles**: Modify `ctx.fillStyle` and `ctx.strokeStyle` to change landmark and connection colors.
- **Detection Parameters**: Adjust `minDetectionConfidence` and `minTrackingConfidence` for more reliable detection.

## Requirements

- A modern browser with WebRTC support (e.g., Chrome, Edge).
- Webcam access permission.

## Potential Enhancements

- Draw connections between landmarks to form a skeleton.
- Detect gestures and trigger custom actions.
- Optimize performance for mobile devices.

## License

This project is open-source and available under the MIT License.

