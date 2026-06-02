from fastapi import FastAPI

from routes import employee_router
app = FastAPI()

app.include_router(employee_router)

