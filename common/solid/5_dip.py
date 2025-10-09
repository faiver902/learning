from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass


class MySQLDatabase(AbstractDatabase):
    def save(self, data):
        return f"Сохраняю в MySQL: {data}"

    def delete(self, data):
        return f"Удаляю что то из бд MySQLDatabase {data}"


class NewSqlDb(AbstractDatabase):
    def delete(self, data):
        return f"Удаляю что то из бд NewSqlDb {data}"

    def save(self, data):
        return f"Сохраняю в NewSqlDb: {data}"


class FakeDatabase(AbstractDatabase):
    def save(self, data):
        return f"[FAKE] Не сохраняю: {data}"

    def delete(self, data):
        return f"Удаляю что то из бд FakeDatabase{data}"


class UserService:
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def create_user(self, name):
        return self.db.save({"name": name})

    def delete(self, name):
        return self.db.delete({"name": name})


fake = FakeDatabase()
service = UserService(fake)
print(service.create_user("Тест"))

db = MySQLDatabase()
service = UserService(db)
print(service.create_user("Иван"))

new_sql = NewSqlDb()
service = UserService(new_sql)
print(service.delete("Vova"))
