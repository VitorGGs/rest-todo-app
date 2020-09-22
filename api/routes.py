from api import api, db
from api.models import Task
from flask import request, jsonify



@api.route('/', methods=['POST'])
def create():
	task = request.form.get('task')
	if task:
		todo = Task(task=task)
		db.session.add(todo)
		db.session.commit()
		return {'message': 'Task created'}, 201
	return {'message': 'No task send.'}, 404


@api.route('/<id>', methods=['GET'])
def read(id):
	task = Task.query.get(id)
	if task:
		response = {
			'id': task.id,
			'task': task.task
		}
		return jsonify(task=response), 200
	return {"message": "Task not found."}, 404


@api.route('/<id>', methods=['PUT'])
def update(id=None):
	task = Task.query.get(id)
	if task:
		if request.form.get('task'):
			task.task = request.form.get('task')
		db.session.commit()
		return {'message': 'The task has been updated.'}, 200

	return {'message': 'task not found.'}, 404


@api.route('/<id>', methods=['DELETE'])
def delete(id):
	task = Task.query.get(id)
	if task:
		db.session.delete(task)
		db.session.commit()
		return {"message": "your task has been deleted"}, 200
	return {'message': 'task not found.'}, 404
