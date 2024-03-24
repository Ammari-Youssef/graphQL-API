import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import *

class ResponseField(graphene.ObjectType):
    message = graphene.String()
    status = graphene.Int()
    
class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class TaskObject(SQLAlchemyObjectType):
    class Meta:
        model = Task

  
class UserProfileObject(SQLAlchemyObjectType):
    class Meta:
        model = UserProfile
        interfaces = (graphene.relay.Node, )
