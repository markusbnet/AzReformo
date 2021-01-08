from fastapi import FastAPI, Form, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

from auth import CREDENTIALS
from storage import storage_list

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
        "dashboard.html", {"request": request, "numbers": storage_list()}
    )  # request must be passed
