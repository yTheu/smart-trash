import cv2
from ultralytics import YOLO
from scripts.mapping import material_mapping

# Carrega o modelo treinado
model = YOLO("best.pt")

# Inicia a captura de vídeo pela webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[int(box.cls)]
            material = material_mapping.get(label, "Outro")  # Pega o tipo de material

            conf = float(box.conf)
            if conf > 0.5:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{material} {conf * 100:.1f}%", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2) 

    
    cv2.imshow("Detecção", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
