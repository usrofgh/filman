from sqladmin import ModelView

from src.domains.associations.production_rating import ProductionRatingAssociation as PPA


class ProductionRatingAdmin(ModelView, model=PPA):
    icon = "fa-solid fa-star"
    name = "Production Rating"

    page_size = 50
    page_size_options = [25, 50, 100]


    column_list = [
        PPA.id,
        PPA.production,
        PPA.rating_company,
        PPA.count_votes,
        PPA.rating,
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
    ]

    column_sortable_list = [
        PPA.production,
    ]

    form_columns = [
        PPA.production,
        PPA.rating_company,
        PPA.count_votes,
        PPA.rating,
    ]