#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request


# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET', 'POST'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    ## Should have at least one parameter in request body
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    # task[0]['title'] = request.json.get('title', task[0]['title'])
    # task[0]['description'] = request.json.get('description', task[0]['description'])
    # task[0]['done'] = request.json.get('done', task[0]['done'])
    # return jsonify({'task': make_public_task(task[0]) } )
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

