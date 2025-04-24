import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from src.admin_panel.auth import authentication_backend
from src.admin_panel.category import CategoryAdmin
from src.admin_panel.comment import CommentAdmin
from src.admin_panel.country import CountryAdmin
from src.admin_panel.genre import GenreAdmin
from src.admin_panel.person import PersonAdmin
from src.admin_panel.production import ProductionAdmin
from src.admin_panel.production_person import ProductionPersonAdmin
from src.admin_panel.production_rating import ProductionRatingAdmin
from src.admin_panel.rating_company import RatingCompanyAdmin
from src.admin_panel.role import RoleAdmin
from src.admin_panel.trailer import TrailerAdmin
from src.admin_panel.user import UserAdmin
from src.api.v1.router import v1_router
from src.core.config import settings
from src.core.db import engine

app = FastAPI()
app.include_router(v1_router)

admin = Admin(app, engine, authentication_backend=authentication_backend)
admin_pages = [
    UserAdmin, ProductionAdmin, TrailerAdmin, CategoryAdmin, GenreAdmin, PersonAdmin,
    RoleAdmin, RatingCompanyAdmin, CountryAdmin, CommentAdmin, ProductionPersonAdmin, ProductionRatingAdmin
]
[admin.add_view(page) for page in admin_pages]

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.API_HOST, port=settings.API_PORT)
