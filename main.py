from flask import Flask, jsonify, render_template
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load social networks data from JSON file
with open('social_networks.json', 'r') as file:
    social_networks = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/social-networks', methods=['GET'])
def get_social_networks():
    return jsonify(social_networks)

if __name__ == '__main__':
    app.run(debug=True)