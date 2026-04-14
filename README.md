# 🖐️ Hand Gesture Interaction System

An interactive real-time hand gesture system that tracks both hands and generates dynamic visual feedback based on finger movements. The system creates an **elastic band simulation** that responds naturally to hand motion.

---

## 🚀 Features

* 🔍 **Real-time Hand Tracking**

  * Detects and tracks both hands simultaneously
  * Works smoothly with live camera input

* ✋ **21 Hand Landmarks Detection**

  * Tracks all key points: thumb, index, middle, ring, and pinky
  * High-precision fingertip tracking

* 🎯 **Dynamic Fingertip Tracking**

  * Continuously updates fingertip positions
  * Enables responsive interaction

* 🧠 **Noise Reduction & Stability**

  * Reduces jitter in hand tracking
  * Provides smooth and stable motion output

* 🎨 **Interactive Visual Feedback**

  * Generates an **elastic band effect**
  * Visual reacts in real-time to hand movement

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe (for hand tracking)
* NumPy

---

## ⚙️ How It Works

1. Captures video input from webcam
2. Detects hand landmarks (21 points per hand)
3. Tracks fingertip positions dynamically
4. Applies smoothing techniques to reduce noise
5. Maps hand movement to an elastic band simulation
6. Renders interactive visual feedback in real-time

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/hand-gesture-system.git

# Navigate to project folder
cd hand-gesture-system

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

* Make sure your webcam is enabled
* Use your hands in front of the camera to interact

---

## 📸 Demo

(Add screenshots or GIFs here)

---

## 🧪 Future Improvements

* Gesture recognition (pinch, zoom, swipe)
* Physics-based simulation for realistic elastic behavior
* Multi-hand interaction enhancements
* Integration with AR/VR systems

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* MediaPipe for hand tracking
* OpenCV for computer vision tools

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---
