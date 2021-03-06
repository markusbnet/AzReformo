import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from azure.mgmt.storage.v2019_04_01.models import StorageAccount
from fastapi import BackgroundTasks, FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

# database
import models
from auth import CREDENTIALS
from config import settings
from database import engine
from storage import (create_storage, get_latest_storage,
                     get_storage_properties, storage_remediations)

app = FastAPI()
templates = Jinja2Templates(directory="templates/pages")


@app.on_event("startup")
async def startup_event():
    models.Base.metadata.create_all(bind=engine)
    create_storage()  # gather storage on startup


@app.get("/")
def home_get(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": CREDENTIALS}
    )  # request must be passed


@app.get("/dashboard")
def dashboard_get(request: Request):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request}
    )  # request must be passed


@app.get("/storage")
def storage_get(request: Request):
    return templates.TemplateResponse(
        "storage.html", {"request": request, "storage_accounts": get_latest_storage()}
    )  # request must be passed


@app.get("/storage/{storage_id}")
def storage_get_id(request: Request, storage_id: str):
    return templates.TemplateResponse(
        "storageid.html",
        {
            "request": request,
            "storage": get_storage_properties(storage_id),
            "banner": False,
        },
    )  # request must be passed


@app.post("/storage/{storage_id}")
async def storage_update(
    request: Request,
    background_tasks: BackgroundTasks,
    storage_id: str,
    action: str = Form("action"),
):
    background_tasks.add_task(storage_remediations, storage_id, action)
    return templates.TemplateResponse(
        "storageid.html",
        {
            "request": request,
            "storage": get_storage_properties(storage_id),
            "banner": True,
        },
    )  # request must be passed


scheduler = BackgroundScheduler()
# this will move when the pr is complete. should be on a schedule.
scheduler.add_job(create_storage, "interval", minutes=settings.app_data_refresh)
scheduler.start()
