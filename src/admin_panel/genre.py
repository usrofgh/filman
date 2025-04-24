from sqladmin import ModelView

from src.domains.genres.models import GenreModel


class GenreAdmin(ModelView, model=GenreModel):
    icon = "fa-solid fa-tags"
    name = "Genre"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_list = [
        GenreModel.id,
        GenreModel.name,
        GenreModel.description,
        GenreModel.productions,
        GenreModel.created_at,
        GenreModel.updated_at
    ]
    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        GenreModel.name
    ]

    column_sortable_list = [
        GenreModel.name
    ]

    form_columns = [
        GenreModel.name,
        GenreModel.description,
    ]
