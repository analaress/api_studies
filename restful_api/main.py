import requests
import json
import tarefa


url = 'https://brasilapi.com.br/api/fipe/marcas/v1/'

def buscar_dados():
    request = requests.get(url)
    todos = json.loads(request)
    # todos = request.json()
    print(todos)
    print(todos[0]['nome'])

def cadastrar_dados():
    requests.post(url,
                  json=(tarefa.__dict__))

def editar_dados(id, tarefa):
    requests.put(url, f"id={id}",
                 json=(tarefa.__dict__))

def remover_dados(id):
    requests.delete(url, f"id={id}")


if __name__ == '__main__':
    buscar_dados()

