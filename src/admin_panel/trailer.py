from sqladmin import ModelView

from src.domains.trailers.models import TrailerModel


class TrailerAdmin(ModelView, model=TrailerModel):
    icon = "fa-solid fa-play"
    name = "Trailer"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_list = [
        TrailerModel.id,
        TrailerModel.production,
        TrailerModel.duration_sec,
        TrailerModel.video_url,
        TrailerModel.created_at,
        TrailerModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        TrailerModel.production,
    ]

    column_sortable_list = [
        TrailerModel.production
    ]

    form_columns = [
        TrailerModel.production,
        TrailerModel.duration_sec,
        TrailerModel.video_url,
    ]