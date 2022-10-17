from fastapi import FastAPI
from routes.user import user


app = FastAPI(
    title= "API PRUEBA-MYSQL",
    description="Api para insertar usuarios en base de datos mysql en servidor apache con XAMPP"
)
app.include_router(user)
