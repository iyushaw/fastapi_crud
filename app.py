import os, sys
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schemas import AuthorSchema, PostSchema, UpdateAuthorSchema, UpdatePostSchema
from models import Post, Author

app = FastAPI()
load_dotenv(".env")
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
def index():
    return {"message": "welcome"}

@app.post("/api/post", response_model=PostSchema)
def make_post(post: PostSchema):
    db_post = Post(title=post.title, content=post.content, author_id=post.author_id)
    db.session.add(db_post)
    db.session.commit()
    return db_post

@app.post("/api/author", response_model=AuthorSchema)
def make_author(author: AuthorSchema):
    db_author = Author(name=author.name, age=author.age, rating=author.rating)
    db.session.add(db_author)
    db.session.commit()
    return db_author

@app.get("/api/posts")
def posts():
    posts = db.session.query(Post).all()
    return posts

@app.get("/api/authors")
def authors():
    authors = db.session.query(Author).all()
    return authors

@app.get("/api/post/{id}")
def get_post_by_id(id: str):
    return {"message": "Post with {id}!"}


@app.put("/api/post/{id}", response_model=UpdatePostSchema)
def update_post(id: int, updated_post: UpdatePostSchema):
    post = db.session.query(Post).filter(Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not Found!")
    
    post.title = updated_post.title
    post.content = updated_post.content
    db.session.commit()

    return post

@app.put("/api/author/{id}", response_model=AuthorSchema)
def update_post(id: int, updated_author: AuthorSchema):
    author = db.session.query(Author).filter(Author.id == id).first()

    if author is None:
        raise HTTPException(status_code=404, detail="Author not Found!")
    
    author.title = updated_author.name
    author.content = updated_author.age
    db.session.commit()

    return author


# Route for Deleting Post
@app.delete("/api/post/{id}", status_code=204)
def delete_post(id: str):
    delete_post = db.session.query(Post).filter(Post.id == id).first()

    if not delete_post:
        raise HTTPException(status_code=404, detail="Post Not Found!")
    db.session.delete(delete_post)
    db.session.commit()

    return delete_post