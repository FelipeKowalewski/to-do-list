from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.exceptions import InternalDatabaseError
from app.database.database import Base, engine
from app.routers import auth, tasks


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(InternalDatabaseError)
async def sqlalchemy_exception_handler(
    request: Request,
    exc: InternalDatabaseError
):
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno no banco de dados"}
    )


Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(tasks.router)
