from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.startup import build_faiss

from app.routers.auth import router as auth_router
from app.routers.resume import router as resume_router
from app.routers.job import router as job_router
from app.routers.candidate import router as candidate_router
from app.routers.export import router as export_router
from app.routers.dashboard import router as dashboard_router
from app.routers.summary import router as summary_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("\n🚀 Application Starting...")

    build_faiss()

    print("✅ FAISS Loaded")

    yield

    print("👋 Application Shutdown")


app = FastAPI(
    title="AI Resume Screening API",
    version="1.0.0",
    lifespan=lifespan
)

# Register Routers
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(candidate_router)
app.include_router(export_router)
app.include_router(dashboard_router)
app.include_router(summary_router)


@app.get("/")
def root():

    return {
        "message": "AI Resume Screening API",
        "status": "Running",
        "version": "1.0.0"
    }