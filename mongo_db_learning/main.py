from typing import List

from beanie import Document, Insert, Replace, before_event
from bson import ObjectId
from pydantic import Field


class Category(Document):
    name: str
    slug: str
    parent_id: ObjectId | None = None
    ancestors: List[ObjectId] = Field(default_factory=list)
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
