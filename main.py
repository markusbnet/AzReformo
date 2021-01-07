from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from auth import CREDENTIALS

app = FastAPI()
templates = Jinja2Templates(directory="templates/pages/")

numbers = [
    1,
    2,
    3,
]


@app.get("/")
def home_get(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": CREDENTIALS}
    )  # request must be passed


@app.get("/dashboard")
def dashboard_get(request: Request):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "numbers": numbers}
    )  # request must be passed
