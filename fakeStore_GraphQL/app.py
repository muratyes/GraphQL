from flask import Flask, render_template
import requests
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

app = Flask(__name__)

# Rick and Morty GraphQL endpoint
url = 'https://rickandmortyapi.com/graphql'

# GraphQL transport
transport = RequestsHTTPTransport(url=url, use_json=True)

# Client'ı başlat
client = Client(transport=transport, fetch_schema_from_transport=True)

# GraphQL sorgusu
query = gql("""
{
  characters {
    results {
      id
      name
      species
      image
    }
  }
}
""")

# Verileri çek
def get_characters():
    try:
        result = client.execute(query)
        characters = result['characters']['results']
        return characters
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

@app.route('/')
def index():
    characters = get_characters()
    return render_template('index.html', characters=characters)

if __name__ == '__main__':
    app.run(debug=True)
