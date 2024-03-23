# schema.py

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import *

class User(SQLAlchemyObjectType):
    class Meta:
        model = User

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        age = graphene.Int(required=True)

    user = graphene.Field(User)

    def mutate(self, info, username, email):
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            raise Exception('Username already exists')

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return AddUser(user=new_user)
    
class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()
    
class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
