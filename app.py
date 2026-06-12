from fastapi import FastAPI

from routes import employee_router, contract_router, worklog_router, payroll_router, login_router
app = FastAPI()

app.include_router(employee_router)
app.include_router(contract_router)
app.include_router(worklog_router)
app.include_router(payroll_router)
app.include_router(login_router)
