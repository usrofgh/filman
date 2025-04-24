from sqladmin import ModelView

from src.domains.countries.models import CountryModel


class CountryAdmin(ModelView, model=CountryModel):
    icon = "fa-solid fa-flag"
    name = "Country"
    name_plural = "Countries"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_labels = {
        CountryModel.persons: "Born in this country",
    }
    column_list = [
        CountryModel.id,
        CountryModel.country_code,
        CountryModel.name,
        CountryModel.productions,
        CountryModel.persons,
        CountryModel.created_at,
        CountryModel.updated_at
    ]

    column_details_list = [
        *column_list
    ]

    column_searchable_list = [
        CountryModel.name,
    ]

    column_sortable_list = [
        CountryModel.country_code,
        CountryModel.name
    ]

    form_columns = [
        CountryModel.country_code,
        CountryModel.name
    ]