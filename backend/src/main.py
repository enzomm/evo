from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.configs.settings import settings
from src.routes import router


def ApplicationFactory() -> FastAPI:
    """Init App Factory FastAPI"""
    application = FastAPI(title=settings.TITLE,docs_url="/api/docs", redoc_url="/api/redoc")

    # register middlewares
    origins = ["*"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register Routes
    application.include_router(router, prefix="/api/v1")

    return application


app = ApplicationFactory()


@app.get("/")
def check_health():
    return {"OK": True}
