# schema.py

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from mutations import *


class Query(graphene.ObjectType):
    users = graphene.List(UserObject)
    tasks = graphene.List(TaskObject)
    
    def resolve_users(self, info):
        return User.query.all()
    
    def resolve_tasks(self, info):
        return Task.query.all()

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_task = AddTask.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
