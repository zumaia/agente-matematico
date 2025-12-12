# 🧠 Math Agent - Multi-Agent System for Mathematical Reasoning

> **A2A-Compliant Agentic AI System** | AgentX-AgentBeats Ready

**Hybrid multi-agent architecture** that solves mathematical problems through intelligent orchestration between algorithmic solvers and AI reasoning. Built for the [Berkeley RDI AgentX Competition](https://rdi.berkeley.edu/agentx-agentbeats).

## 🏗️ Agentic Architecture

### Multi-Agent System
- **🧮 Purple Agent** (`app.py:8000`) - **Solver Agent**: Mathematical reasoning with hybrid orchestration
- **📊 Green Agent** (`green_app.py:8001`) - **Evaluator Agent**: Specialized assessment and benchmarking
- **🔄 A2A Protocol**: Full compliance with Agent-to-Agent communication standards

### Intelligent Orchestration
```python
# Agentic decision-making process
resolutores_priorizados = priorizar_resolutores(problema, resolutores_base)
for resolutor in resolutores_priorizados:
    solucion = resolutor(problema)  # Dynamic tool selection
```

## 🚀 Quick Start

### Docker (Recommended)
```bash
echo "GROQ_API_KEY=your_key_here" > .env  # Optional AI fallback
docker-compose up --build
```
**Access:**
- Purple Agent: http://localhost:8000
- Green Evaluator: http://localhost:8001

### Local Development
```bash
git clone https://github.com/zumaia/agente-matematico.git
cd agente-matematico
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py  # Purple Agent
python green_app.py  # Green Evaluator (separate terminal)
```

## 🧪 AgentX Competition Features

### A2A Standard Endpoints
```bash
# Agent Discovery
GET /agent-card    # Agent metadata & capabilities
POST /reset        # State reset for reproducible evaluation
GET /api           # Health check & A2A compliance

# Evaluation Endpoints (Green Agent)
POST /evaluate     # Standard AgentBeats evaluation (English)
POST /evaluate-es  # Spanish evaluation endpoint
```

### Automated Evaluation
```bash
# Run complete evaluation suite
python scripts/run_local_eval.py

# Or via Docker
docker-compose exec -T green python3 scripts/run_local_eval.py
```

## 🛠️ Technical Capabilities

### Mathematical Domains
- **Algebra**: Equations, matrices, determinants
- **Geometry**: Areas, volumes, Pythagorean theorem  
- **Statistics**: Mean, median, mode, probability
- **Trigonometry**: Sine, cosine, tangent functions
- **Calculus**: Function analysis, roots, sequences

### Agentic Patterns Implemented
- **Tool-Using Agent**: 15+ specialized mathematical tools
- **Orchestrator Router**: Intelligent solver prioritization
- **Hybrid Reasoning**: Algorithmic + AI fallback strategy
- **Multi-Agent Collaboration**: Purple-Green agent interaction

## 📊 Performance Features

- **Intelligent Caching**: Plausibility-checked solution caching
- **Multi-language Support**: ES, EN, EU
- **Educational Focus**: ESO/Bachillerato curriculum alignment
- **Real-time Visualization**: Mathematical graphing capabilities

## 🔧 API Usage

### Solve Mathematical Problems
```bash
curl -X POST "http://localhost:8000/resolver-web" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "problema=Resolver la ecuación 2x + 5 = 13&lang=es"
```

### Evaluate Agent Performance
```bash
curl -X POST "http://localhost:8001/evaluate" \
  -H "Content-Type: application/json" \
  -d '{
    "purple_agent_url": "http://purple:8000",
    "num_problemas": 5,
    "categoria": "algebra"
  }'
```

## 🏆 Competition Ready

This system demonstrates **production-grade Agentic AI** with:
- ✅ A2A protocol compliance
- ✅ Reproducible evaluation setup
- ✅ Multi-agent architecture
- ✅ Hybrid reasoning capabilities
- ✅ Educational domain specialization

## 📁 Project Structure
```
agente-matematico/
├── app.py                 # Purple Agent (Solver)
├── green_app.py           # Green Agent (Evaluator)
├── matematica/            # Mathematical tools library
│   ├── algebra.py        # Equation solvers
│   ├── geometria.py      # Geometry tools
│   └── estadistica.py    # Statistical functions
├── scripts/
│   └── run_local_eval.py # Evaluation runner
└── docker-compose.yml    # Multi-agent deployment
```

## 👤 Author
**Oscar Rojo** - [GitHub](https://github.com/zumaia)

## 📄 License
MIT License
