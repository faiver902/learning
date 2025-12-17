from typing import Annotated, List

from fastapi import APIRouter, Path, Depends, Body
from fastapi import Query
from pydantic import AfterValidator, BaseModel

test_router = APIRouter(prefix="/test")


class QSchemas(BaseModel):
    q: int


def deps_gt_four(q) -> QSchemas:
    if int(q) < 4:
        return QSchemas(q=1)
    return QSchemas(q=q)


@test_router.get("/annotated_gt_4/")
def annotated(q: QSchemas = Depends(deps_gt_four)):
    return {"message": q.q}


@test_router.get("/gt/")
def gt(q: Annotated[int, Query(description="Some title", gt=4, lt=7)]):
    return {"message": q}


@test_router.post("/list_query")
def list_query(q: Annotated[List[int], Query()]):
    print([i for i in q])
    print(q[3])
    return {"message": q}


def after_valid(value):
    if value > 8:
        return "value gt 8"
    return value


@test_router.get("/test_after_validation")
def test_after_validation(q: Annotated[int, AfterValidator(after_valid)]):
    return {"message": q}

class QueryShema(BaseModel):
    model_config = {"extra": "forbid"}

    q: int

@test_router.get("/query_schema")
def query_schema(q: Annotated[QueryShema, Query()]):
    return {"message": q.q}