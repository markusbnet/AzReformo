from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import datetime
from auth import CREDENTIALS
from storage import storage_list, get_storage, create_storage

# database
import models
from database import engine

app = FastAPI()
templates = Jinja2Templates(directory="templates/pages")


@app.on_event("startup")
async def startup_event():
    models.Base.metadata.create_all(bind=engine)
    create_storage() #gather storage on startup


@app.get("/")
def home_get(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": CREDENTIALS, "storage": get_storage()}
    )  # request must be passed


@app.get("/dashboard")
def dashboard_get(request: Request):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request}
    )  # request must be passed


@app.get("/storage")
def storage_get(request: Request):
    return templates.TemplateResponse(
        "storage.html", {"request": request, "storage_accounts": get_storage()}
    )  # request must be passed


scheduler = BackgroundScheduler()
  # this will move when the pr is complete. should be on a schedule.
scheduler.add_job(create_storage, "interval", minutes=5)
scheduler.start()
