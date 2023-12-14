from flask import Flask
from requests import post

app = Flask(__name__)

@app.route("/user", methods=["POST"])
def createUser():
    
    user = {
        'name': 'Mussarelo',
        'email': 'delicio@email.com',
        'user': 'Mussarelo.delicio'
    }

    response = post('http://localhost:3000/user', json=user)

    print('Resposta da requisição da API Node:', response.json())

    return {"mensagem": "Usuario gerado com a graça de Deus!"}
    
@app.route("/getUsers", methods=["GET"])
def getUsers():
    Users = [
        {
            'name': 'Mussarelo',
            'email': 'delicio@email.com',
            'user': 'Mussarelo.delicio'
        },
        {
            'name': 'Pepperono',
            'email': 'spicy@email.com',
            'user': 'Pepperono.spicy'
        },
        {
            'name': 'Margherito',
            'email': 'classic@email.com',
            'user': 'Margherito.classic'
        },
        {
            'name': 'Calabreso',
            'email': 'hot@email.com',
            'user': 'Calabreso.hot'
        }
    ]
    return Users

if __name__ == "__main__":
    app.run()
