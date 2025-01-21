from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


try:
    templates = Jinja2Templates(directory="templates")
except Exception as e:
    print(f"Error loading templates: {e}")
    # Handle the exception or re-raise it


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    try:
        return templates.TemplateResponse(
        name="item.html", context={"request": request, "id": id}
    )
    except Exception as e:
        return HTMLResponse(f"Error rendering template: {e}", status_code=500)
