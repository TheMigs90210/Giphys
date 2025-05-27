from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Substitua pela sua chave da API do Giphy
GIPHY_API_KEY = 'y67aP8zltdDdSH4eYKanV3Oae9xBYbXb'
GIPHY_URL = 'https://api.giphy.com/v1/gifs/search'


@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    if request.method == 'POST':
        search_term = request.form['search_term']
        response = requests.get(GIPHY_URL, params={
            'api_key': GIPHY_API_KEY,
            'q': search_term,
            'limit': 9,  # Mostra mais resultados
            'lang': 'pt'
        })

        if response.status_code == 200:
            gifs = response.json().get('data', [])
        else:
            print(f"Erro ao buscar GIFs: {response.status_code}")

    return render_template('index.html', gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)