# 📥 Guía de Instalación - Agente Matemático

## Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## 🛠️ Instalación Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico

¡Excelente! Vamos a crear una **documentación técnica profesional** para tu agente matemático. 

## 📁 **ESTRUCTURA DE DOCUMENTACIÓN:**


docs/
├── 📄 INSTALLATION.md          # Instalación detallada
├── 📄 API_REFERENCE.md         # Referencia completa de API
├── 📄 ARCHITECTURE.md          # Arquitectura técnica
├── 📄 AGENTX_SETUP.md          # Guía para AgentX Competition
├── 📄 CONTRIBUTING.md          # Guía de contribución
└── 📄 MODULES.md               # Documentación de módulos


## 🚀 **EMPEZAMOS CON LOS ARCHIVOS:**

### **1. Crear carpeta docs:**
```bash
mkdir docs
```

### **2. `docs/INSTALLATION.md` - Instalación Detallada**
```markdown
# 📥 Guía de Instalación - Agente Matemático

## Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## 🛠️ Instalación Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
```bash
# Crear archivo .env
cp .env.example .env
# Editar .env con tus configuraciones
```

**Archivo .env:**
```env
GROQ_API_KEY=tu_api_key_de_groq
DEBUG=True
CACHE_FILE=matematica_cache.json
```

### 5. Ejecutar el Servidor
```bash
python app.py
```

### 6. Verificar Instalación
Abre tu navegador en: `http://localhost:8000`

## 🐳 Instalación con Docker

### Construir Imagen
```bash
docker build -t agente-matematico .
```

### Ejecutar Contenedor
```bash
docker run -p 8000:8000 --env-file .env agente-matematico
```

## 🔧 Solución de Problemas

### Error: Módulo no encontrado
```bash
pip install -r requirements.txt --force-reinstall
```

### Error: Puerto en uso
```bash
# Cambiar puerto
python app.py --port 8080
```

### Error: API Key de Groq
- Verifica que GROQ_API_KEY esté en el archivo .env
- Reinicia el servidor después de cambios

## ✅ Verificación
Visita `http://localhost:8000/api` para confirmar que la API está funcionando.
```

### **3. `docs/API_REFERENCE.md` - Referencia de API**
```markdown
# 🔌 Referencia de API - Agente Matemático

## Endpoints Principales

### `GET /`
**Descripción**: Interfaz web principal  
**Respuesta**: HTML con la interfaz de usuario

### `GET /api`
**Descripción**: Información del agente  
**Respuesta**:
```json
{
  "mensaje": "¡Agente Matemático Mejorado! 🎯",
  "version": "4.0.0",
  "arquitectura": "modular",
  "modulos": ["algebra", "geometria", "aritmetica", "estadistica", "patrones", "cache", "ia"],
  "mejoras": ["+5 funciones estadísticas", "detección de intención", "sistema de cache"]
}
```

### `POST /resolver`
**Descripción**: Resolver problema matemático (JSON)  
**Content-Type**: `application/json`  
**Body**:
```json
{
  "problema": "resolver 2x + 5 = 15"
}
```

**Respuesta Exitosa**:
```json
{
  "problema": "resolver 2x + 5 = 15",
  "solucion": "x = 5",
  "tipo_problema": "ecuacion_lineal",
  "pasos_detallados": ["Paso 1: Restar 5 a ambos lados...", "Paso 2: Dividir por 2..."],
  "metodo": "algoritmo_matematico",
  "estado": "resuelto"
}
```

### `POST /resolver-web`
**Descripción**: Resolver problema matemático (Form)  
**Content-Type**: `application/x-www-form-urlencoded`  
**Body**: `problema=resolver 2x + 5 = 15`  
**Respuesta**: HTML con la solución formateada

### `GET /cache/estado`
**Descripción**: Estado del sistema de cache  
**Respuesta**:
```json
{
  "total_entradas": 15,
  "archivo": "matematica_cache.json"
}
```

### `DELETE /cache/limpiar`
**Descripción**: Limpiar cache del sistema  
**Respuesta**:
```json
{
  "mensaje": "Cache limpiado correctamente"
}
```

## 🔄 Flujo de Resolución

1. **Recepción**: El problema llega por POST
2. **Cache**: Se verifica si ya existe solución en cache
3. **Análisis**: Detección de intención y priorización de resolutores
4. **Resolución**:
   - Primero con algoritmos matemáticos
   - Luego con IA Groq (si está configurada)
5. **Respuesta**: Solución estructurada con pasos detallados

## 📊 Códigos de Estado

- `200 OK`: Solicitud exitosa
- `422 Unprocessable Entity`: Problema mal formado
- `500 Internal Server Error`: Error del servidor

## 🔍 Ejemplos de Uso

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/resolver",
    json={"problema": "calcular área de un círculo con radio 5"}
)
print(response.json())
```

### JavaScript
```javascript
fetch('http://localhost:8000/resolver', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ problema: '2x + 5 = 15' })
})
.then(response => response.json())
.then(data => console.log(data));
```

### cURL
```bash
curl -X POST "http://localhost:8000/resolver" \
     -H "Content-Type: application/json" \
     -d '{"problema": "calcular media de 5, 10, 15"}'
```
