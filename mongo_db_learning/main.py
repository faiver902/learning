import asyncio
from typing import List

from beanie import Document, Insert, Replace, before_event, init_beanie
from bson import ObjectId as _ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import ConfigDict, Field


class Category(Document):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={_ObjectId: str})

    name: str
    slug: str
    parent_id: _ObjectId | None = None
    ancestors: List[_ObjectId] = Field(default_factory=list)
    level: int = 0
    path: str = "/"

    class Settings:
        name = "categories"
        indexes = [
            [("parent_id", 1), ("slug", 1)],  # unique per parent
            [("ancestors", 1)],
            [("path", 1)],
        ]

    @before_event([Insert, Replace])
    async def _compute_paths(self):
        if self.parent_id:
            parent = await Category.get(self.parent_id)
            assert parent, "parent not found"
            self.ancestors = parent.ancestors + [parent.id]
            self.level = parent.level + 1
            self.path = (parent.path.rstrip("/") + f"/{self.slug}").replace("//", "/")
        else:
            self.ancestors = []
            self.level = 0
            self.path = "/" + self.slug.strip("/")


# Примеры запросов:

# создать корень
# await Category(name="Электроника", slug="electronics").insert()

# создать потомка
# await Category(name="Смартфоны", slug="phones", parent_id=root.id).insert()

# дети узла
# children = await Category.find(Category.parent_id == node_id).to_list()

# хлебные крошки
# breadcrumbs = await Category.find(Category.id.in_([*node.ancestors, node.id])).sort("level").to_list()

# всё поддерево
# subtree = await Category.find(Category.ancestors == node_id).to_list()
MONGO_URI = "mongodb://admin:password@localhost:27017"
DB_NAME = "categories"
async def main():
    client = AsyncIOMotorClient(MONGO_URI)
    try:
        db = client[DB_NAME]
        await init_beanie(database=db, document_models=[Category])

        # # 1. Создаём корень
        # root = Category(name="Электроника", slug="electronics")
        # await root.insert()
        # print("root_id:", root.id)
        #
        # # 2. Создаём потомка
        # child = Category(name="Смартфоны", slug="phones", parent_id=root.id)
        # await child.insert()
        # print("child_id:", child.id)

        # # 3. CRUD операции
        # root = await Category.find_one(Category.slug == "electronics")
        # # дети узла
        # children = await Category.find(Category.parent_id == root.id).to_list()
        # print("children:", [c.name for c in children])

        # # хлебные крошки
        # breadcrumbs = await Category.find(
        #     Category.id.in_([*child.ancestors, child.id])
        # ).sort("level").to_list()
        # print("breadcrumbs:", [b.name for b in breadcrumbs])

        # # поддерево
        # subtree = await Category.find(Category.ancestors == root.id).to_list()
        # print("subtree:", [s.name for s in subtree])

        # # апдейт узла
        # child.name = "Смартфоны и гаджеты"
        # await child.save()  # update/replace по _id

        # удалить
        # await child.delete()
    finally:
        client.close()

asyncio.run(main())

asyncio.run(main())
# переместить узел в нового родителя
# 1) загрузить узел, старые значения
# 2) пересчитать для узла ancestors/level/path как в _compute_paths
# 3) сохранить узел
# 4) пачкой обновить потомков на основе нового пути:
# await Category.get_motor_collection().update_many(
#     {"ancestors": node.id},
#     [{
#       "$set": {
#         "ancestors": {
#           "$concatArrays": [
#              new_ancestors,  # список ObjectId
#              {"$slice": ["$ancestors", {"$add": [ {"$indexOfArray": ["$ancestors", node.id]}, 1]} , {"$size": "$ancestors"}]}
#           ]
#         },
#         "level": {"$add": [len(new_ancestors), {"$subtract": ["$level", (old_level)]}]},
#         "path": {
#           "$concat": [new_path_prefix, {"$substr": ["$path", len(old_path_prefix), 10_000]}]
#         }
#       }
#     }]
# )
