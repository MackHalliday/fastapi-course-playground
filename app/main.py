from typing import Optional
from fastapi import FastAPI, status, HTTPException

from pydantic import BaseModel

app = FastAPI()

POST_DATA = {
        1: {
            "title": "Understanding Python Basics",
            "content": "This article covers the fundamentals of Python programming...",
            "rating": 4,
            "published": True,
        },
        2: {
            "title": "Advanced Data Structures in Python",
            "content": "In this guide, we explore complex data structures like heaps...",
            "rating": 5,
            "published": False,
        },
        3: {
            "title": "Introduction to Machine Learning",
            "content": "Machine learning is transforming the tech landscape...",
            "rating": 3,
            "published": True,
        },
    }

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


def find_post(id):
    return POST_DATA.get(id)


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/post")
def get_posts():
    return {"data": "Posts returned."}


@app.get("/post/{id}")
def get_post(id: int):
    post = find_post(id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )
    return {"data": post}


@app.post("/post", status_code=201)
def create_post(post: Post):
    return {"new_post": post}


@app.patch("/post/{id}", status_code=204)
def update_post(id: int, post: Post):
    post = find_post(id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )
    return {"update_post": f"Updated post with id: {id}"}


@app.delete("/post/{id}", status_code=204)
def delete_post(id: int):
    post = find_post(id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )
    return {"delete_post": f"Deleted post with id: {id}"}
