import cv2
from PIL import Image, ImageTk


def start_camera_stream(image_label, stop_flag):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        image_label.config(text="Não foi possível acessar a câmera.")
        return

    while not stop_flag():
        ret, frame = camera.read()

        if not ret:
            image_label.config(text="Erro ao capturar frame.")
            break

        # Redimensionando o frame para caber no widget
        frame = cv2.resize(frame, (640, 480))  # Ajuste conforme necessário
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertendo para o formato compatível com Tkinter
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Atualizando a imagem no label
        image_label.config(image=imgtk, text="")
        image_label.image = imgtk

    camera.release()
    cv2.destroyAllWindows()
