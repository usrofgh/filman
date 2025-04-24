from sqladmin import ModelView

from src.domains.productions.models import ProductionModel


class ProductionAdmin(ModelView, model=ProductionModel):
    icon = "fa-solid fa-film"
    name = "Production"

    page_size = 50
    page_size_options = [25, 50, 100]


    column_labels = {
        ProductionModel.production_person_associations: "Production ↔ Person",
        ProductionModel.rating_associations: "Production ↔ Ratings"
    }

    column_list = [
        ProductionModel.id,
        ProductionModel.name,
        ProductionModel.poster_url,
        ProductionModel.trailer,
        ProductionModel.duration_min,
        ProductionModel.description,
        ProductionModel.release_date,
        ProductionModel.release_year,
        ProductionModel.category,
        ProductionModel.genres,
        ProductionModel.production_person_associations,
        ProductionModel.rating_associations,
        ProductionModel.countries,
        ProductionModel.comments,
        ProductionModel.created_at,
        ProductionModel.updated_at,
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        ProductionModel.name,
    ]

    column_sortable_list = [
        ProductionModel.name
    ]

    form_columns = [
        ProductionModel.name,
        ProductionModel.poster_url,
        ProductionModel.trailer,
        ProductionModel.duration_min,
        ProductionModel.description,
        ProductionModel.release_date,
        ProductionModel.release_year,
        ProductionModel.category,
        ProductionModel.genres,
        ProductionModel.production_person_associations,
        ProductionModel.rating_associations,
        ProductionModel.countries,
        ProductionModel.comments,
    ]
