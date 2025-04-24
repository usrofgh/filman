from sqladmin import ModelView

from src.domains.rating_companies.models import RatingCompanyModel


class RatingCompanyAdmin(ModelView, model=RatingCompanyModel):
    icon = "fa-solid fa-building"
    name = "Rating Company"
    name_plural = "Rating Companies"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_labels = {
        RatingCompanyModel.rating_associations: "Production ↔ Ratings",

    }
    column_list = [
        RatingCompanyModel.id,
        RatingCompanyModel.name,
        RatingCompanyModel.rating_associations,
        RatingCompanyModel.created_at,
        RatingCompanyModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        RatingCompanyModel.name
    ]

    column_sortable_list = [
        RatingCompanyModel.name
    ]

    form_columns = [
        RatingCompanyModel.name
    ]