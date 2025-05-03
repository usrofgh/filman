from sqladmin import ModelView

from src.domains.comment_reactions.models import CommentReactionModel


class CommentReactionAdmin(ModelView, model=CommentReactionModel):
    icon = "fa-solid fa-comment"
    name = "Comment Reaction"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_list = [
        CommentReactionModel.id,
        CommentReactionModel.user,
        CommentReactionModel.comment,
        CommentReactionModel.reaction,
        CommentReactionModel.created_at,
        CommentReactionModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        CommentReactionModel.user,
    ]

    column_sortable_list = [
       CommentReactionModel.user,
       CommentReactionModel.reaction,
       CommentReactionModel.created_at
    ]