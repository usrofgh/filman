from sqladmin import ModelView

from src.domains.roles.models import RoleModel


class RoleAdmin(ModelView, model=RoleModel):
    icon = "fa-solid fa-user-tag"
    name = "Role"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_labels = {
        RoleModel.production_person_associations: "Production ↔ Person",
    }
    column_list = [
        RoleModel.id,
        RoleModel.name,
        RoleModel.production_person_associations,
        RoleModel.created_at,
        RoleModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        RoleModel.name
    ]

    column_sortable_list = [
        RoleModel.name
    ]

    form_columns = [
        RoleModel.name
    ]