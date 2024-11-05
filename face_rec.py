import os
import pickle
import face_recognition
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class FaceRecognitionApp:
    def __init__(self, db_path):
        self.db_path = db_path
        self.known_face_encodings, self.known_face_names = self.load_db()
        self.process_frame_cnt = 0
        self.font = ImageFont.truetype("simhei.ttf", 15)  # 加载中文字体
    def load_db(self):
        db_file = os.path.join(self.db_path, "db.pkl")
        if os.path.exists(db_file):
            with open(db_file, 'rb') as f:
                known_face_encodings, known_face_names = pickle.load(f)
            return known_face_encodings, known_face_names
        else:
            img_names = os.listdir(self.db_path)
            known_face_encodings = []
            known_face_names = []
            for img_name in img_names:
                img_path = os.path.join(self.db_path, img_name)
                img = face_recognition.load_image_file(img_path)
                face_encoding = face_recognition.face_encodings(img)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(os.path.splitext(img_name)[0])
            with open(db_file, 'wb') as f:
                pickle.dump((known_face_encodings, known_face_names), f)
            return known_face_encodings, known_face_names

    def process_frame(self, frame):
        if self.process_frame_cnt == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]+f"confidence:{1 - face_distances[best_match_index]:.2f}"
                self.face_names.append(name)
            self.process_frame_cnt = 5
        else:
            self.process_frame_cnt -= 1

        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_img)

        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # 绘制人脸框
            draw.rectangle([(left, top), (right, bottom)], outline=(0, 0, 255), width=2)
            draw.rectangle([(left, bottom - 20), (right, bottom)], fill=(0, 0, 255))

            # 绘制中文文本
            draw.text((left + 6, bottom - 20), name, font=self.font, fill=(255, 255, 255, 255))

        return pil_img
        # for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # return frame
