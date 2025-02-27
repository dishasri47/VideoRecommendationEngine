from flask import Flask, render_template, request, jsonify
from recommendation import get_youtube_recommendations  # Import function from recommendation.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form.get('query')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    recommendations = get_youtube_recommendations(query)
    
    if not recommendations:
        return jsonify({"error": "No recommendations found. Try another search!"}), 404

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
