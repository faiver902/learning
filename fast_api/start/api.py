import os
from typing import Annotated

import aiofiles
from starlette import status
from starlette.responses import StreamingResponse
from pathlib import Path

from database.db import get_db
from database.models import Person
from fastapi import APIRouter, Body, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session

start_router = APIRouter()


@start_router.get("/")
def read_root():
    return {"message": "Hello METANIT.COM"}


@start_router.get("/")
def main():
    return FileResponse("public/index.html")


@start_router.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Person).all()


@start_router.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=404, content={"message": "Пользователь не найден"}
        )
    # если пользователь найден, отправляем его
    return person


@start_router.post("/api/users")
def create_person(data=Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], age=data["age"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@start_router.put("/api/users")
def edit_person(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=404, content={"message": "Пользователь не найден"}
        )
    person.age = data["age"]
    person.name = data["name"]
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person


@start_router.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person is None:
        return JSONResponse(
            status_code=404, content={"message": "Пользователь не найден"}
        )

    # если пользователь найден, удаляем его
    db.delete(person)  # удаляем объект
    db.commit()  # сохраняем изменения
    return person




