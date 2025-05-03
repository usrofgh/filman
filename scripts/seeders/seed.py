import asyncio
import datetime
import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.base_model import BaseModel
from src.core.db import session_maker
from src.domains.associations.production_person import ProductionPersonAssociation
from src.domains.associations.production_rating import ProductionRatingAssociation
from src.domains.categories.models import CategoryModel
from src.domains.comment_reactions.models import CommentReactionModel
from src.domains.comments.models import CommentModel
from src.domains.countries.models import CountryModel
from src.domains.genres.models import GenreModel
from src.domains.persons.models import PersonModel
from src.domains.productions.models import ProductionModel
from src.domains.rating_companies.models import RatingCompanyModel
from src.domains.roles.models import RoleModel
from src.domains.trailers.models import TrailerModel
from src.domains.users.models import UserModel

SEED_CONFIG = [
    ("users.json", UserModel),
    ("genres.json", GenreModel),
    ("categories.json", CategoryModel),
    ("countries.json", CountryModel),
    ("roles.json", RoleModel),
    ("rating_companies.json", RatingCompanyModel),
    ("persons.json", PersonModel),
    ("productions.json", ProductionModel),
    ("trailers.json", TrailerModel),

    ("production_person.json", ProductionPersonAssociation),
    ("production_rating.json", ProductionRatingAssociation),
    ("comments.json", CommentModel),
    ("comment_reactions.json", CommentReactionModel)
]

MODEL_MAPPINGS = {
    "ProductionModel": ProductionModel,
    "CountryModel": CountryModel,
    "PersonModel": PersonModel,
    "RoleModel": RoleModel,
    "GenreModel": GenreModel,
    "CategoryModel": CategoryModel,
    "TrailerModel": TrailerModel,
    "ProductionPersonAssociation": ProductionPersonAssociation,
    "RatingCompanyModel": RatingCompanyModel,
    "CommentModel": CommentModel,
    "CommentReactionModel": CommentReactionModel,
    "UserModel": UserModel,
}


def load_json(file_path: Path) -> list[dict]:
    with open(file_path, "r") as file:
        data = json.loads(file.read())
        return data


def fields_to_date_format(el: dict) -> None:
    for key, value in el.items():
        if key in ["birthdate", "release_date"]:
            year, month, day = [int(v) for v in value.split("-")]
            el[key] = datetime.date(year, month, day)


async def proceed_deps(session: AsyncSession, el: dict, deps: list) -> None:
    for dep in deps:

        # Take from
        lookup_model = MODEL_MAPPINGS[dep["lookup_model"]]
        print(lookup_model)
        lookup_value = el.pop(dep["source"])
        # Insert into
        lookup_field = dep["lookup_field"]
        target = dep["target"]
        model_field = getattr(lookup_model, lookup_field)

        stmt = select(lookup_model)
        if isinstance(lookup_value, list) is False:
            stmt = stmt.where(model_field == lookup_value)
            res = (await session.execute(stmt)).scalars().first()
            el[target] = str(res.id)
        else:
            stmt = stmt.where(model_field.in_(lookup_value))
            res = (await session.execute(stmt)).scalars().all()
            el[target] = res


async def insert_table_data(session: AsyncSession, file_name: str, model: BaseModel) -> None:
    file_path = Path(__file__).parent.joinpath("data").joinpath(file_name)
    data = load_json(file_path)

    deps = data[0].get("deps")
    if deps:
        del data[0]

    for el in data:
        fields_to_date_format(el)
        if deps:
            await proceed_deps(session, el, deps)

    session.add_all([model(**el) for el in data])


async def main():
    async with session_maker() as session:
        for table_info in SEED_CONFIG:
            await insert_table_data(session, *table_info)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
