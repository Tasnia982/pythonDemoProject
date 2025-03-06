import cv2
import matplotlib.pyplot as plt

def detect_faces_in_image(image_path):
    """Detect faces in an image file."""
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load the image. Check the file path.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title("Face Detection (Image)")
    plt.show()

def detect_faces_in_webcam():
    """Detect faces in real-time using a webcam."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow("Face Detection (Webcam)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Select an option:")
    print("1 - Detect faces in an image")
    print("2 - Detect faces in real-time using a webcam")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        image_path = input("Enter the full image path: ").strip()
        detect_faces_in_image(image_path)
    elif choice == "2":
        detect_faces_in_webcam()
    else:
        print("Invalid choice. Please run the script again and enter 1 or 2.")
