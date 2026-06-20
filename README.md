# DETECCION-DE-BOTELLAS

# Integrantes

Daniel Cortes Villa-23310392
Byron Zadquiel Flores Gonzalez-23310338

# Instrucciones para correr el código

# Clonar el repositorio
git clone https://github.com/usuario/Detector-Botellas.git
cd Detector-Botellas

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
Colocar en la terminal las siguientes lineas:

sudo apt-get update && sudo apt-get install -y libgl1
pip install ultralytics

# Ejecutar entrenamiento o pruebas
python train.py

# Problema a resolver
En una línea de producción de botellas, es necesario contar automáticamente las unidades que pasan por la banda transportadora. El conteo manual es ineficiente y propenso a errores, lo que afecta la productividad y la trazabilidad.

# Flujo de funcionamiento
-La cámara captura imágenes de las botellas en movimiento.
-El modelo YOLO detecta cada botella en tiempo real.
-El sistema incrementa el contador por cada detección válida.
-El conteo se muestra en pantalla y se guarda en un registro digital.
-El sistema puede reiniciarse mediante un botón físico o software para iniciar un nuevo lote.

# Beneficios
-Reducción de errores humanos en el conteo.
-Mejora en la trazabilidad y control de producción.
-Posibilidad de integración con sistemas SCADA o ERP para análisis de datos.