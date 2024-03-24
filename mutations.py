import graphene
from objects import *

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserObject)
    response = graphene.Field(ResponseField)

    def mutate(self, info, **kwargs):
        try:
            existing_user = User.query.filter_by(username=kwargs['username']).first()
            if existing_user:
                raise Exception('Username already exists')

            new_user = User(**kwargs)
            db.session.add(new_user)
            db.session.commit()

            return AddUser(user=new_user, response=ResponseField(message='User added successfully', status=200))
        except Exception as e:
            db.session.rollback()
            return AddUser(user=None, response=ResponseField(message=str(e), status=400))


class AddTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        due_date = graphene.String(required=True)
        user_id = graphene.Int(required=True)

    task = graphene.Field(TaskObject)
    response = graphene.Field(ResponseField)

    def mutate(self, info, **kwargs):
        try:
            new_task = Task(**kwargs)
            db.session.add(new_task)
            db.session.commit()

            return AddTask(task=new_task, response=ResponseField(message='Task added successfully', status=200))
        except Exception as e:
            db.session.rollback()
            return AddTask(task=None, response=ResponseField(message=str(e), status=400))