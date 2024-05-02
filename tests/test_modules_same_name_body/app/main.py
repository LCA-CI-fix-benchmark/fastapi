from fastapi import FastAPI

from . import module_a, module_b

app = FastAPI()

app.include_router(module_a.router, prefix="/a")
app.include_router(module_b.router, prefix="/b")