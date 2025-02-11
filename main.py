import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt") # Carrega o modelo
cap =cv2.VideoCapture(0) # Inicia a captura de vídeo

while cap.isOpened():
    ret, frame = cap.read() # Se a captura estiver funcionando, lê o que vê nela
    frame = cv2.resize(frame, (640, 480)) # Redimensionar para menor resolução e maior FPS

    if not ret:
        break

    results = model(frame) # Passa os dados da captura, lida pelo modelo, para os resultados

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0]) # Coordenadas
            label = model.names[int(box.cls)] # Nomes
            conf = float(box.conf) # Para selecionar apenas objetos que tem confiança do que é (Se tem certeza que ta vendo uma pedra...)

            if conf > 0.5: # Confiança maior que 50%
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf * 100:.1f}%", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Detecção", frame) # Roda a captura e detecção

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

