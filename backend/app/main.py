from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ---------------------------------------------------
# API ROUTES
# ---------------------------------------------------

from app.api.generate_session import (
    router as session_router
)

# ---------------------------------------------------
# FASTAPI APP
# ---------------------------------------------------

app = FastAPI(

    title="OPTISWIMM API",

    description="""
    OPTISWIMM
    AI High Performance Swimming System

    Features:
    - Adaptive session generation
    - Fatigue analysis
    - Readiness analysis
    - Performance prediction
    - Intelligent periodization
    - CNS management
    - Injury prevention
    - Adaptive microcycles
    """,

    version="2.0.0"
)

# ---------------------------------------------------
# CORS CONFIGURATION
# ---------------------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# ---------------------------------------------------
# INCLUDE ROUTERS
# ---------------------------------------------------

app.include_router(

    session_router,

    prefix="/api",

    tags=["Session Generator"]
)

# ---------------------------------------------------
# ROOT ROUTE
# ---------------------------------------------------

@app.get("/")

def root():

    return {

        "application":
        "OPTISWIMM",

        "status":
        "online",

        "version":
        "2.0.0",

        "docs":
        "/docs"
    }

# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------

@app.get("/health")

def health_check():

    return {

        "status":
        "healthy"
    }

# ---------------------------------------------------
# API INFO
# ---------------------------------------------------

@app.get("/api-info")

def api_info():

    return {

        "name":
        "OPTISWIMM API",

        "features": [

            "Adaptive Sessions",

            "Fatigue Engine",

            "Readiness Engine",

            "Performance Prediction",

            "Constraint Engine",

            "Microcycle Builder",

            "Periodization Engine",

            "Injury Prevention"
        ]
    }

# ---------------------------------------------------
# STARTUP EVENT
# ---------------------------------------------------

@app.on_event("startup")

async def startup_event():

    print("\n")
    print("====================================")
    print("OPTISWIMM API STARTED")
    print("====================================")
    print("Swagger Docs:")
    print("http://127.0.0.1:8000/docs")
    print("====================================")
    print("\n")

# ---------------------------------------------------
# SHUTDOWN EVENT
# ---------------------------------------------------

@app.on_event("shutdown")

async def shutdown_event():

    print("\n")
    print("====================================")
    print("OPTISWIMM API STOPPED")
    print("====================================")
    print("\n")