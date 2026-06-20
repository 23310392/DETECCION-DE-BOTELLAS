
from ultralytics import YOLO
import os

DATASET_YAML = "dataset/data.yaml"  
MODELO_BASE  = "yolov8n.pt"           
EPOCHS       = 50
BATCH        = 8                       
IMG_SIZE     = 640


if not os.path.exists(DATASET_YAML):
    print(f" No se encontró")
else:
    print(f" Dataset encontrado: {DATASET_YAML}")

    model = YOLO(MODELO_BASE)

    resultados = model.train(
        data=DATASET_YAML,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH,
        patience=10,
        name="mi_modelo_v2",
        device="cpu",
        workers=2,
    )
    print(f" Resultados guardados en: {resultados.save_dir}")