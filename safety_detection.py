# --------------- construction safety Detection -------------------

from ultralytics import YOLO
import cv2
import pandas as pd
import pygame

path_alarm = r"C:\Users\osama\OneDrive\Desktop\Moahmmed Upwork\mixkit-facility-alarm-sound-999.wav"
pygame.init()
pygame.mixer.music.load(path_alarm)

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture(r'C:\Users\osama\OneDrive\Desktop\Moahmmed Upwork\Civil Engineering Technician Career Video.mp4')
model = YOLO(r'C:\Users\osama\Downloads\construction safety.pt')
class_list = {0: 'Helmet', 1: 'No Helmet', 2: 'No Vest', 3: 'Person', 4: 'Vest'}

person_axis = []
count = 0

while True:
    _, image = video.read()
    if image is None:  # Break the loop if the video ends
        break

    image_copy = image.copy()
    h, w, c = image.shape

    image = cv2.flip(image, 1)
    result = model.predict(image)

    a = result[0].boxes.data
    px = pd.DataFrame(a).astype(float)

    # Flags to check if "No Helmet" or "No Vest" is detected
    no_helmet_detected = False
    no_vest_detected = False

    for index, row in px.iterrows():
        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
        cls = class_list[int(row[5])]
        confidence = row[4]

        if confidence <= 0.4:
            continue

        if cls == 'No Helmet':
            no_helmet_detected = True
        elif cls == 'No Vest':
            no_vest_detected = True

        if cls in ('Helmet', 'Vest', 'Person'):
            if cls == 'Person':
                person_axis.append((x1, y1, x2, y2))
                count += 1
            color = (0, 255, 0)
        elif cls in ('No Helmet', 'No Vest'):
            color = (0, 0, 255)
        else:
            continue

        if color == (0, 0, 255) and len(person_axis) >= 1:
            x11, y11, x22, y22 = person_axis[count - 1]
            person_status = image_copy[y11:y22, x1:x22]
            cv2.imwrite(rf'D:\Construction-Safety\images\person{count}.png', person_status)

        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(image, (x1, y1 - 25), (x1 + 200, y1), color, -1)

        cv2.putText(image, f'id:{index}', (x1, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)
        cv2.putText(image, f'{cls}', (x1 + 55, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)
        cv2.putText(image, f'{round(confidence, 2)}', (x1 + 150, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)

    # Control the alarm sound based on detection flags
    if no_helmet_detected or no_vest_detected:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    else:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('o'):
        break

cv2.destroyAllWindows()
video.release()