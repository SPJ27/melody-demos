from melody.db import Database, Table, CharField

db = Database()


class Todo(Table):
    title = CharField()
    description = CharField()


db.register([Todo])


def create(req):
    todo = Todo.create(
        title=req.headers['title'],
        description=req.headers['description']
    )

    return {
        'success': True,
        'data': todo.id
    }


def read(req):
    todos = Todo.select()

    return {
        'success': True,
        'data': [
            {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description
            }
            for todo in todos
        ]
    }


def update(req):
    todo = Todo.get_by_id(req.query['id'])

    todo.title = req.query['title']
    todo.description = req.query['description']
    todo.save()

    return {
        'success': True,
        'data': {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description
        }
    }


def delete(req):
    todo = Todo.get_by_id(req.query['id'])
    todo.delete_instance()

    return {
        'success': True
    }


routes = {
    'POST /new': create,
    'GET /': read,
    'PUT /update': update,
    'DELETE /delete': delete
}