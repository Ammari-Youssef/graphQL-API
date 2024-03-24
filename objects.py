import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import *

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class TaskObject(SQLAlchemyObjectType):
    class Meta:
        model = Task
        
class ResponseField(graphene.ObjectType):
    message = graphene.String()
    status = graphene.Int()
