import wtforms
from sqladmin import ModelView

from src.domains.users.models import UserModel


class UserAdmin(ModelView, model=UserModel):
    icon = "fa-solid fa-user"

    name = "User"

    page_size = 50
    page_size_options = [25, 50, 100]
    form_overrides = dict(email=wtforms.EmailField)
    column_list = [
        UserModel.id,
        UserModel.email,
        UserModel.is_active,
        UserModel.is_admin,
        UserModel.comments,
        UserModel.comment_reactions,
        UserModel.created_at,
        UserModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        UserModel.email,
    ]

    column_sortable_list = [
        UserModel.created_at,
        UserModel.updated_at
    ]

    form_columns = [
        UserModel.email,
        UserModel.is_admin,
        UserModel.is_active
    ]