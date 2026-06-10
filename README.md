```md
# 🚨 AELP — Autonomous Emergency Logistics Planner

AELP is a full-stack, event-driven logistics intelligence platform designed for **real-time emergency response optimization in dynamic and disrupted environments**.

It models a live **digital twin of a geographical region** and prepares the foundation for:

- Vehicle Routing Optimization (VRP)
- Resource Allocation (Linear / Integer Programming)
- Model Predictive Control (MPC)
- Event-driven simulation of disasters
- Real-time GIS dashboards
- AI-assisted operational decision support (future phase)

This repository contains **Week 1: Core System Foundation (Production Scaffold)**.

---

# 🧠 Core Idea (First Principles)

Emergency logistics is fundamentally:

```

State + Constraints + Objectives → Optimal Decisions

```

Where:

- **State** → Vehicles, depots, demand, roads, events
- **Constraints** → Capacity, time, fuel, accessibility
- **Objectives** → Minimize delay, maximize coverage, reduce cost
- **Decisions** → Routes, allocations, dispatch actions

AELP is designed to continuously recompute decisions as state changes.

---

# 🏗️ System Architecture (Week 1)

```

```
                     ┌────────────────────┐
                     │   React Frontend   │
                     │   (Leaflet GIS)    │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │   FastAPI Backend  │
                     │   API Gateway      │
                     └─────────┬──────────┘
                               │
    ┌──────────────────────────┼──────────────────────────┐
    ▼                          ▼                          ▼
```

┌──────────────┐        ┌──────────────┐         ┌──────────────┐
│ Fleet API    │        │ Depot API    │         │ Demand API   │
└──────┬───────┘        └──────┬───────┘         └──────┬───────┘
│                       │                          │
└───────────────────────┴──────────────────────────┘
▼
┌────────────────────────┐
│ PostgreSQL + PostGIS  │
│ (Geospatial DB Layer)  │
└────────────────────────┘

````

---

# ⚙️ Tech Stack

## Backend
- FastAPI (Python)
- SQLAlchemy ORM
- Pydantic v2
- PyJWT Authentication
- Uvicorn ASGI Server

## Frontend
- React 19
- Vite
- TypeScript
- Leaflet (GIS visualization)
- Material UI (UI components)

## Database
- PostgreSQL
- PostGIS (Geospatial extensions)

## Infrastructure
- Docker
- Docker Compose

---

# 📦 Features Implemented (Week 1)

## Backend
- FastAPI modular architecture
- Fleet / Depot / Demand APIs
- JWT authentication scaffold
- SQLAlchemy base models
- DB session management
- Clean API versioning (/api/v1)

## Frontend
- React + Vite setup
- Interactive GIS map (Leaflet)
- Default location centered (Munich)
- Extensible UI structure for future overlays

## Infrastructure
- Fully containerized system
- PostgreSQL + PostGIS ready
- Backend + frontend orchestration via Docker Compose

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/aelp.git
cd aelp
````

---

## 2. Setup Environment Variables

```bash
cp .env.example .env
```

---

## 3. Run Full System

```bash
docker compose up --build
```

or

```bash
make up
```

---

# 🌐 Access Services

| Service      | URL                                                          |
| ------------ | ------------------------------------------------------------ |
| Frontend     | [http://localhost:3000](http://localhost:3000)               |
| Backend API  | [http://localhost:8000/docs](http://localhost:8000/docs)     |
| Health Check | [http://localhost:8000/health](http://localhost:8000/health) |
| Database     | localhost:5432                                               |

---

# 📡 API Overview

## 🔹 Fleet API

```http
GET  /api/v1/fleet
POST /api/v1/fleet
```

---

## 🔹 Depot API

```http
GET  /api/v1/depots
POST /api/v1/depots
```

---

## 🔹 Demand API

```http
GET  /api/v1/demand
POST /api/v1/demand
```

---

## 🔹 Auth API

```http
POST /api/v1/auth/login
```

### Default Credentials

```
username: admin
password: admin
```

---

# 🧪 Example Payloads

## 🚚 Vehicle

```json
{
  "name": "Truck-01",
  "vehicle_type": "truck",
  "capacity": 1200,
  "fuel_level": 0.8,
  "latitude": 48.13,
  "longitude": 11.58,
  "status": "idle"
}
```

---

## 🏭 Depot

```json
{
  "name": "Depot A",
  "latitude": 48.14,
  "longitude": 11.56
}
```

---

## 🧭 Demand Point

```json
{
  "name": "Hospital Zone A",
  "priority": 5,
  "location": {
    "lat": 48.135,
    "lng": 11.57
  },
  "resource_demand": {
    "food": 100,
    "water": 200
  },
  "criticality": "high"
}
```

---

# 🧠 Design Principles

## 1. Digital Twin First

All system decisions originate from a consistent world state model.

## 2. Event-Driven Ready

System is designed to evolve toward event sourcing and real-time updates.

## 3. Optimization Layer Isolation

Routing and allocation engines will be pluggable modules (not hardcoded).

## 4. MPC-Ready Architecture

System is designed for future rolling horizon optimization.

---

# 🧱 What is NOT included (Week 1 Scope)

To maintain clean architecture:

* ❌ No OR-Tools / VRP yet
* ❌ No MPC controller yet
* ❌ No event streaming (Redis/Kafka) yet
* ❌ No simulation engine yet
* ❌ No AI copilot yet
* ❌ No Kubernetes / Terraform yet

These will be added progressively in later weeks.

---

# 🗺️ Frontend Capabilities

* Interactive GIS map (Leaflet)
* Base geospatial rendering
* Ready for overlays:

  * Vehicles
  * Depots
  * Demand zones
  * Events (floods, closures)
  * Route visualization

---

# 📊 System Maturity (Week 1)

| Component      | Status        |
| -------------- | ------------- |
| Frontend GIS   | ✅ Done        |
| Backend API    | ✅ Done        |
| Database Setup | ⚠️ Basic      |
| Optimization   | ❌ Not started |
| Simulation     | ❌ Not started |
| MPC            | ❌ Not started |
| AI Copilot     | ❌ Not started |

---

# 🧭 Roadmap

## Week 2

* Real PostgreSQL schema
* Fleet persistence layer
* PostGIS geometry integration
* Map ↔ DB synchronization

## Week 3–4

* OR-Tools VRP engine
* Resource allocation solver (LP/MILP)

## Week 5–6

* Event-driven simulation engine
* Digital twin state reconstruction

## Week 7+

* MPC rolling horizon controller
* AI Copilot (LangGraph + RAG)
* Production scaling (Kubernetes + Terraform)

---

# ⚠️ Important Note

This is a **foundational scaffold**, not a finished logistics system.

It is intentionally designed to evolve into:

> A real-time autonomous emergency logistics operating system.

---

# 👨‍💻 License

MIT (or define later)

---
