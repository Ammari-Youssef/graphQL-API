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

    def mutate(self, info, title, description, due_date, user_id):
        try:
            # Check if user with the provided user_id exists
            user = User.query.get(user_id)
            if not user:
                raise Exception('User not found')

            new_task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return AddTask(task=new_task, response=ResponseField(message='Task added successfully', status=200))
        except Exception as e:
            db.session.rollback()
            return AddTask(task=None, response=ResponseField(message=str(e), status=400))

class AddUserProfile(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        sexe = graphene.String(required=True)
        birth_date = graphene.String(required=True)
        age = graphene.Int(required=True)
        user_id = graphene.Int(required=True)

    profile = graphene.Field(UserProfileObject)
    response = graphene.Field(ResponseField)

    def mutate(self, info, **kwargs):
        try:
            new_profile = UserProfile(**kwargs)
            db.session.add(new_profile)
            db.session.commit()

            return AddUserProfile(profile=new_profile, response=ResponseField(message='Profile added successfully', status=200))
        except Exception as e:
            db.session.rollback()
            return AddUserProfile(profile=None, response=ResponseField(message=str(e), status=400))
        

## Update Mutations 
from sqlalchemy.orm.exc import NoResultFound

class UpdateTask(graphene.Mutation):
    class Arguments:
        task_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        due_date = graphene.DateTime()

    task = graphene.Field(TaskObject)
    response = graphene.Field(ResponseField)

    def mutate(self, info, task_id, title=None, description=None, due_date=None):
        task = Task.query.get(task_id)
        if task is None:
            raise NoResultFound(f'Task with id: {task_id} not found')
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date

        db.session.commit()

        return UpdateTask(task=task, response=ResponseField(message='Task updated successfully', status=200))