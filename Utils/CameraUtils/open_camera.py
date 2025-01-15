import cv2


def open_camera():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Não foi possivel acessar a camera")
        exit()

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Erro ao capturar frame.")
            break

        cv2.imshow("Feed da Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
