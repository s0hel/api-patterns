from typing import List, Optional

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

USER_STORE = [
    {"name": "Patrick", "age": 100},
    {"name": "Teresa", "age": 80},
    {"name": "Guido", "age": 60},
    {"name": "John", "age": 40}
]


@strawberry.type
class User:
    name: str
    age: int


@strawberry.input
class UserInput:
    name: Optional[str] = strawberry.UNSET
    age: Optional[int] = strawberry.UNSET


@strawberry.type
class Query:
    @strawberry.field
    def user(self, where: UserInput) -> List[User]:
        print(where)
        filtered_users = USER_STORE

        if where.name:
            filtered_users = [user for user in filtered_users if user["name"] == where.name]
        if where.age:
            filtered_users = [user for user in filtered_users if user["age"] == where.age]

        return [User(name=user["name"], age=user["age"]) for user in filtered_users]


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
