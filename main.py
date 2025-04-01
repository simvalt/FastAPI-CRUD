from fastapi import FastAPI
from app.api.routes.api import router
from app.api.core.settings.openapi import tags_metadata

app = FastAPI(
    title="Users API",
    description="FastAPi CRUD",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(router)
