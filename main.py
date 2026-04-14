import cv2
import mediapipe as mp
import numpy as np

# Colors for each finger
colors = [
    (255, 0, 0),    # Thumb - Blue
    (0, 255, 0),    # Index - Green
    (0, 0, 255),    # Middle - Red
    (255, 255, 0),  # Ring - Cyan
    (255, 0, 255)   # Pinky - Magenta
]

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Finger tips
finger_ids = [4, 8, 12, 16, 20]

# Smoothing + dead zone
prev_dists = [0, 0, 0, 0, 0]
alpha = 0.7
threshold = 5

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    all_points = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            h, w, _ = frame.shape
            points = []

            for fid in finger_ids:
                x = int(hand_landmarks.landmark[fid].x * w)
                y = int(hand_landmarks.landmark[fid].y * h)
                points.append((x, y))

                cv2.circle(frame, (x, y), 6, (0, 255, 0), -1)

            all_points.append(points)

    # Draw bands if 2 hands detected
    if len(all_points) == 2:
        hand1, hand2 = all_points

        for i in range(5):
            p1 = hand1[i]
            p2 = hand2[i]

            raw_dist = np.hypot(p2[0] - p1[0], p2[1] - p1[1])

            # smoothing
            smoothed = alpha * prev_dists[i] + (1 - alpha) * raw_dist

            # dead zone
            if abs(smoothed - prev_dists[i]) < threshold:
                dist = prev_dists[i]
            else:
                dist = smoothed

            prev_dists[i] = dist
            dist = int(dist)

            # thickness based on stretch
            thickness = int(np.interp(dist, [50, 300], [2, 10]))

            # dynamic color based on stretch
            base_color = colors[i]
            intensity = int(np.interp(dist, [50, 300], [100, 255]))
            color = tuple(min(255, int(c * intensity / 255)) for c in base_color)

            # draw band
            cv2.line(frame, p1, p2, color, thickness)

            # show distance
            cv2.putText(frame, str(dist), p1,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    cv2.imshow("Hand Interaction - Colored Bands", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()