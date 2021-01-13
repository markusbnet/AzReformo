from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

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
    storage_list()


@app.get("/")
def home_get(request: Request):
    create_storage()  # this will move when the pr is complete. should be on a schedule.
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
scheduler.add_job(storage_list, "interval", minutes=1)
scheduler.start()
