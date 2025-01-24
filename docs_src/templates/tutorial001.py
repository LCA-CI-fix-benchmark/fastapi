from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    # Ensure the template exists and context is set correctly
    template_name = "item.html"
    if not templates.template_exists(template_name):
        raise HTTPException(status_code=404, detail="Template not found")

    return templates.TemplateResponse(
        name=template_name, context={"request": request, "id": id}
    )
