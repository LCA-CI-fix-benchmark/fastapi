from fastapi import FastAPI

from . import a, b

app = FastAPI()

# Include routers with correct prefixes
app.include_router(a.router, prefix="/a")
app.include_router(b.router, prefix="/b")

# Add any necessary adjustments based on CI test failure logs