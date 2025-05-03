from sqladmin import ModelView

from src.domains.productions.models import ProductionModel


class ProductionAdmin(ModelView, model=ProductionModel):
    icon = "fa-solid fa-film"
    name = "Production"

    page_size = 50
    page_size_options = [25, 50, 100]


    column_labels = {
        ProductionModel.production_person_associations: "Cast",
        ProductionModel.rating_associations: "Ratings"
    }

    column_list = [
        ProductionModel.id,
        ProductionModel.name,
        ProductionModel.poster_url,
        ProductionModel.trailer,
        ProductionModel.duration_min,
        ProductionModel.description,
        ProductionModel.release_date,
        ProductionModel.category,
        ProductionModel.genres,
        ProductionModel.rating_associations,
        ProductionModel.countries,
        ProductionModel.created_at,
        ProductionModel.updated_at,
    ]

    column_details_list = [
        *column_list,
        ProductionModel.favorited_by,
        ProductionModel.comments,
        ProductionModel.production_person_associations,
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
        ProductionModel.duration_min,
        ProductionModel.description,
        ProductionModel.release_date,
        ProductionModel.category,
        ProductionModel.genres,
        ProductionModel.countries,
        ProductionModel.favorited_by,
    ]


