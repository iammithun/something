import requests 
import numpy as np
import cv2

while True:
    response = requests.get("http://192.168.1.4:8080/short.jpg")  # Corrected syntax for requests.get
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)  # Corrected syntax for np.array and np.uint8
    render = cv2.imdecode(image_array, -1)  # Corrected syntax for cv2.imdecode
    cv2.imshow('frame', render)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Corrected syntax for cv2.waitKey and comparison
        break
