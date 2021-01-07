from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/pages/")


numbers = [1,2,3,4]

@app.get('/')
def read_form():
    return 'hello world'

@app.get("/page")
def page_get(request: Request):
    return templates.TemplateResponse('base.html', {"request": request, "numbers": numbers}) # request must be passed

