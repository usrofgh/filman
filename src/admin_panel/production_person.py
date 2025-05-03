from sqladmin import ModelView

from src.domains.associations.production_person import ProductionPersonAssociation as PPA


class ProductionPersonAdmin(ModelView, model=PPA):
    icon = "fa-solid fa-user-friends"
    name = "Production Person"

    page_size = 50
    page_size_options = [25, 50, 100]


    column_list = [
        PPA.id,
        PPA.production,
        PPA.person,
        PPA.role,
        PPA.actor_name,
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        PPA.actor_name
    ]

    column_sortable_list = [
        PPA.production,
        PPA.person,
        PPA.role,
    ]

    form_columns = [
        PPA.production,
        PPA.person,
        PPA.role,
    ]