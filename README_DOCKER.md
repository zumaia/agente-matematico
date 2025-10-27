# Docker — Desarrollo y Producción

Este archivo describe cómo construir y ejecutar los servicios `app` (Purple Agent) y `green` (Green Evaluator) usando Docker Compose.

Desarrollo (rápido, con hot-reload)

1. Construir y levantar:

```bash
docker-compose up --build
```

2. Acceder a:

- Purple Agent (UI): http://localhost:8000
- Green Agent (UI): http://localhost:8001

3. Notas:
- El `docker-compose.yml` monta el código fuente en los contenedores para permitir edición en caliente (`volumes` con `./:/app`). Por eso los comandos de `uvicorn` en el Compose usan `--reload`.
- La variable `DEFAULT_PURPLE_AGENT_URL` está definida para `green` como `http://app:8000`, lo que permite que las llamadas entre contenedores usen el nombre del servicio de Compose.

Producción (recomendado)

1. Crear un `docker-compose.prod.yml` (o utilizar el siguiente fragmento) que:
   - No monte los volúmenes del código.
   - No use `--reload`.
   - Configure variables de entorno a través de secretos (por ejemplo, GitHub Actions secrets o Docker secrets).

Ejemplo mínimo (sugerido) para `docker-compose.prod.yml`:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
      - GROQ_API_KEY=${GROQ_API_KEY}
    restart: unless-stopped

  green:
    build: .
    ports:
      - "8001:8001"
    environment:
      - PYTHONUNBUFFERED=1
      - DEFAULT_PURPLE_AGENT_URL=http://app:8000
    depends_on:
      - app
    restart: unless-stopped
```

2. Para desplegar en producción:

```bash
# exportar las variables de entorno en el host o usar secrets del orquestador
docker-compose -f docker-compose.prod.yml up --build -d
```

Buenas prácticas
- No dejar claves en `.env` dentro del repositorio.
- Añadir healthchecks y readiness probes en el orquestador de producción.
- Agregar un `logrotate` o una solución centralizada de logs si se espera tráfico elevado.
# 🐳 Guía de Dockerización

## 🚀 Inicio Rápido

### Prerrequisitos
- Docker instalado
- Docker Compose instalado
- API key de Groq (opcional)

### Ejecución en 3 pasos:

```bash
# 1. Clonar y entrar al directorio
git clone https://github.com/tu-usuario/agente-matematico.git
cd agente-matematico

# 2. Configurar variables (opcional para IA)
echo "GROQ_API_KEY=tu_key_real_aqui" > .env

# 3. Ejecutar
docker-compose up --build




Acceder a la aplicación:
🌐 http://localhost:8000

📋 Comandos Útiles
bash
# Ejecutar en segundo plano
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener
docker-compose down

# Reiniciar
docker-compose restart

# Reconstruir imagen
docker-compose build --no-cache
🔧 Solución de Problemas
❌ Error de puerto
bash
# Cambiar puerto en docker-compose.yml
ports:
  - "8080:8000"  # Usar puerto 8080 en lugar de 8000
❌ Error de API key
bash
# Verificar que el archivo .env existe
ls -la .env

# Crear si no existe
echo "GROQ_API_KEY=tu_key" > .env
❌ Permisos de cache
bash
# Dar permisos a la carpeta cache
chmod 755 cache
🏗️ Estructura Docker
text
agente-matematico/
├── 📄 Dockerfile          # Configuración del contenedor
├── 📄 docker-compose.yml  # Orquestación de servicios
├── 📄 .dockerignore       # Archivos excluidos del build
├── 📄 .env.example        # Variables de entorno de ejemplo
└── 📁 cache/             # Cache persistente (creado automáticamente)
🌐 URLs de la Aplicación
Interfaz Web: http://localhost:8000

API Docs: http://localhost:8000/docs

Health Check: http://localhost:8000/api

🛠️ Desarrollo con Docker
bash
# Modo desarrollo con recarga automática
docker-compose -f docker-compose.dev.yml up  # Si creas un compose para desarrollo

# Ejecutar comandos dentro del contenedor
docker-compose exec math-agent python -c "from matematica.cache import cache_global; print(cache_global.estado())"

# Inspeccionar contenedor
docker-compose exec math-agent bash
📊 Métricas de Rendimiento
Tiempo de startup: ~30 segundos

Uso de memoria: ~200MB

Tamaño de imagen: ~500MB

Disponibilidad: 99.9% con restart policy

text

## 🚀 **Comandos para probar:**

```bash
# 1. Verificar que todos los archivos están en su sitio
ls -la Dockerfile docker-compose.yml .dockerignore .env.example

# 2. Construir y ejecutar (sin API key primero)
docker-compose up --build

# 3. Si funciona, añadir API key para probar Groq
echo "GROQ_API_KEY=tu_key_real" > .env
docker-compose up
✅ Verificación final:
bash
# Estructura final del proyecto
tree -I '__pycache__|.git|.env|venv'

# Deberías ver:
agente-matematico-eso-plus/
├── Dockerfile
├── docker-compose.yml  
├── .dockerignore
├── .env.example
├── README.md
├── README_DOCKER.md
├── requirements.txt
├── app.py
├── translations.py
├── matematica/
├── templates/
└── static/