from typing import Any, Optional

import pytest
from fastapi import APIRouter, FastAPI
from pydantic import AnyUrl, EmailStr

from anyforce.api import PublicAPI

from .model import Model2, name

pytest_plugins = [
    "anyforce.test.fixtures",
]


@pytest.fixture(scope="session")
def models():
    return [name]


@pytest.fixture(scope="session")
def router(app: FastAPI):
    class CreateForm(Model2.form()):
        text_field: AnyUrl

    class UpdateForm(Model2.detail(required_override=False)):
        text_field: Optional[EmailStr]

    class API(PublicAPI[Model2, CreateForm, UpdateForm]):
        def __init__(self) -> None:
            super().__init__(Model2, CreateForm, UpdateForm)

        async def after_create(self, user: str, obj: Model2, input: CreateForm) -> Any:
            obj = await super().after_create(user, obj, input)
            if obj.id == 1:
                return Model2.detail().from_orm(obj)

        async def after_update(self, user: str, obj: Model2, input: UpdateForm) -> Any:
            obj = await super().after_update(user, obj, input)
            if obj.id == 1:
                return Model2.detail().from_orm(obj)

        async def before_delete(self, user: str, obj: Model2) -> Any:
            obj = await super().before_delete(user, obj)
            new_obj = await Model2.filter(id=obj.id).first()
            assert new_obj
            return new_obj

    router = APIRouter(prefix="/models")
    API().bind(router)
    app.include_router(router)
    return router
