from sqladmin import ModelView

from src.domains.comments.models import CommentModel


class CommentAdmin(ModelView, model=CommentModel):
    icon = "fa-solid fa-comment"
    name = "Comment"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_list = [
        CommentModel.id,
        CommentModel.user,
        CommentModel.production,
        CommentModel.content,
        CommentModel.created_at,
        CommentModel.updated_at
    ]

    column_details_list = [
        *column_list,
        CommentModel.reactions
    ]

    column_searchable_list = [
        CommentModel.user,
    ]

    column_sortable_list = [
        CommentModel.user,
        CommentModel.production,
        CommentModel.created_at
    ]

    form_columns = [
        CommentModel.production,
        CommentModel.content,
    ]
