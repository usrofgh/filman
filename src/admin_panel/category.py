from sqladmin import ModelView

from src.domains.categories.models import CategoryModel


class CategoryAdmin(ModelView, model=CategoryModel):
    icon = "fa-solid fa-list"
    name = "Category"
    name_plural = "Categories"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_list = [
        CategoryModel.id,
        CategoryModel.name,
        CategoryModel.productions
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        CategoryModel.name,
        CategoryModel.productions,
    ]

    column_sortable_list = [
        CategoryModel.name,
        CategoryModel.created_at,
    ]

    form_columns = [
        CategoryModel.name,
        CategoryModel.productions,
    ]