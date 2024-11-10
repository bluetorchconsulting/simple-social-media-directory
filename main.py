from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load social networks data from JSON file
with open('social_networks.json', 'r') as file:
    social_networks = json.load(file)

@app.route('/api/social-networks', methods=['GET'])
def get_social_networks():
    return jsonify(social_networks)

if __name__ == '__main__':
    app.run(debug=True)
