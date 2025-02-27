from flask import Flask, render_template, request, jsonify
import difflib

app = Flask(__name__)

# Sample video dataset (Replace with a real dataset or API later)
videos = [
    "Flask Web Development",
    "Machine Learning Basics",
    "Deep Learning Guide",
    "Data Science Overview",
    "Python for Beginners",
    "AI and Machine Learning Crash Course",
    "Web Development with Flask and Django",
    "Introduction to Neural Networks",
]

def get_recommendations(search_query):
    """
    Returns the best matching videos. If no exact match is found,
    it suggests the most relevant ones.
    """
    search_query = search_query.lower()
    matches = [video for video in videos if search_query in video.lower()]
    
    if matches:
        return matches  # Return matching results
    
    # If no exact match, return similar titles using fuzzy matching
    close_matches = difflib.get_close_matches(search_query, videos, n=3, cutoff=0.2)
    
    if close_matches:
        return close_matches  # Return similar results
    
    # If nothing is close enough, return some default recommendations
    return ["Recommended: Python Programming Basics", "Recommended: AI Concepts", "Recommended: Tech Trends"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_input = request.form.get("video_title", "")
    
    if not user_input:
        return jsonify({"error": "Please enter a video title."})
    
    recommendations = get_recommendations(user_input)
    
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
