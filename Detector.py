from ultralytics import YOLO

# ─── CONFIGURACIÓN ───────────────────────────────────────
MODELO = "runs/detect/mi_modelo_v2/weights/best.pt"
FUENTE  = "Prueba"  
CONFIANZA = 0.6                 


model = YOLO(MODELO)

resultados = model.predict(
    source=FUENTE,
    conf=CONFIANZA,
    save=True,        # guarda imágenes con las detecciones
    save_txt=True,    # guarda las coordenadas en .txt
    show_conf=True,   # muestra el porcentaje de confianza
)

print("\n Proceso finalizado!!!")
print(f"Resultados en: runs/detect/predict/")

for det in resultados:
    print(f"  {det.path.split('/')[-1]} → {len(det.boxes)} botellas")