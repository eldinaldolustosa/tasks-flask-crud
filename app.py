from flask import Flask, request, jsonify
from models.task import Task
#__name__ = '__main__'
app = Flask(__name__)

#CRUD [Create, Read, Update, Delete]
#Table: Task

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data.get('title'),description=data.get('description',''))
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    #return 'Nova tarefa criada com sucesso.'
    return jsonify({'mensagem':'Nova tarefa criada com sucesso.'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    #task_list = [task.to_dict() for task in tasks]
    for task in tasks:
        task_list.append(task.to_dict())
    output = {
                'tasks': task_list,
                'total_tasks': len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({'Mensagem': 'Nao foi possivel encontrar a tarefa'}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({'mensagem': 'Nao foi possivel encontrar a tarefa id : '}), 404
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.description = data['completed']
    print(task)
    return jsonify({'mensagem': 'Tarefa atualizada com sucesso'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if not task:
        return jsonify({'mensagem': 'Nao foi possivel encontrar a tarefa. '}), 404
    tasks.remove(task)
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'})

@app.route('/user/<int:user_id>')
def show_user(user_id):
    print(user_id)
    print(type(user_id))
    return "%s" % user_id

if  __name__ == '__main__':
    app.run(debug=True)