from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from storage import load_todos, save_todos

# Charger les tâches depuis le fichier JSON
todos = load_todos()

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/todos':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'todos': todos}).encode('utf-8'))
        elif self.path.startswith('/todos/'):
            try:
                todo_id = int(self.path.split('/')[-1])
                todo = next((t for t in todos if t['id'] == todo_id), None)
                if todo is None:
                    self.send_response(404)
                    self.wfile.write(json.dumps({'error': 'Todo not found'}).encode('utf-8'))
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'todo': todo}).encode('utf-8'))
            except ValueError:
                self.send_response(400)
                self.wfile.write(json.dumps({'error': 'Invalid ID'}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/todos':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(post_data)
                title = data['title']
                todo = {
                    'id': (max(t['id'] for t in todos) + 1) if todos else 1,
                    'title': title,
                    'completed': False
                }
                todos.append(todo)
                save_todos(todos)  # Sauvegarder les tâches mises à jour
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'todo': todo}).encode('utf-8'))
            except (json.JSONDecodeError, KeyError):
                self.send_response(400)
                self.wfile.write(json.dumps({'error': 'Bad request'}).encode('utf-8'))

    def do_PUT(self):
        if self.path.startswith('/todos/'):
            try:
                todo_id = int(self.path.split('/')[-1])
                todo = next((t for t in todos if t['id'] == todo_id), None)
                if todo is None:
                    self.send_response(404)
                    self.wfile.write(json.dumps({'error': 'Todo not found'}).encode('utf-8'))
                    return
                content_length = int(self.headers['Content-Length'])
                put_data = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(put_data)
                if 'title' in data:
                    todo['title'] = data['title']
                if 'completed' in data:
                    todo['completed'] = data['completed']
                save_todos(todos)  # Sauvegarder les tâches mises à jour
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'todo': todo}).encode('utf-8'))
            except (ValueError, json.JSONDecodeError):
                self.send_response(400)
                self.wfile.write(json.dumps({'error': 'Bad request'}).encode('utf-8'))

    def do_DELETE(self):
        if self.path.startswith('/todos/'):
            try:
                todo_id = int(self.path.split('/')[-1])
                # index = None
                # for i,t in enumerate(todos):
                #     if t['id'] == todo_id:
                #         index = t['id']
                index = next((i for i, t in enumerate(todos) if t['id'] == todo_id), None)
                if index is None:
                    self.send_response(404)
                    self.wfile.write(json.dumps({'error': 'Todo not found'}).encode('utf-8'))
                    return
                del todos[index]
                save_todos(todos)  # Sauvegarder les tâches mises à jour
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({'result': True}).encode('utf-8'))
            except ValueError:
                self.send_response(400)
                self.wfile.write(json.dumps({'error': 'Invalid ID'}).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=TodoHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
