# schema.py

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from mutations import *
from models import *

class Query(graphene.ObjectType):
    users = graphene.List(UserObject)
    tasks = graphene.List(TaskObject)
    profiles = graphene.List(UserProfileObject)
    
    def resolve_users(self, info):
        return User.query.all()
    
    def resolve_tasks(self, info):
        return Task.query.all()
    
    def resolve_profiles(self, info):
        return UserProfile.query.all()
class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    
    add_user_profile = AddUserProfile.Field()
    update_user_profile = UpdateUserProfile.Field()
    delete_user_profile = DeleteUserProfile.Field()
    
    add_task = AddTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
