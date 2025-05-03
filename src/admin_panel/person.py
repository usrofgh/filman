from sqladmin import ModelView

from src.domains.persons.models import PersonModel


class PersonAdmin(ModelView, model=PersonModel):
    icon = "fa-solid fa-user"
    name = "Person"

    page_size = 50
    page_size_options = [25, 50, 100]

    column_labels = {
        PersonModel.production_person_associations: "Productions"
    }


    column_list = [
        PersonModel.id,
        PersonModel.name,
        PersonModel.birthdate,
        PersonModel.birth_country,
        PersonModel.photo_url,
        PersonModel.created_at,
        PersonModel.updated_at
    ]

    column_details_list = [
        *column_list,
        PersonModel.production_person_associations,
    ]

    column_searchable_list = [
        PersonModel.name
    ]

    column_sortable_list = [
        PersonModel.name
    ]

    form_columns = [
        PersonModel.name,
        PersonModel.birthdate,
        PersonModel.birth_country,
        PersonModel.photo_url
    ]