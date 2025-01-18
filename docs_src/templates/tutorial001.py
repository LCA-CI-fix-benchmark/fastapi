import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Ensure template and static directories exist
templates_dir = "templates"
static_dir = "static"

if not os.path.exists(static_dir):
    os.makedirs(static_dir)

if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    template_path = Path(templates_dir) / "item.html"
    if not template_path.exists():
        return JSONResponse(
            status_code=500,
            content={"message": "Template file not found"}
        )
    try:
        return templates.TemplateResponse(
            name="item.html", 
            context={"request": request, "id": id}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Template rendering error: {str(e)}"}
        )
