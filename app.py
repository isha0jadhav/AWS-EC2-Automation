from flask import Flask

# Create Flask application
app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Web App 🚀</h1>
    <p>This is a simple Flask application.</p>
    <a href="/about">Go to About Page</a>
    """

# About Route
@app.route("/about")
def about():
    return """
    <h2>About</h2>
    <p>This web app is built using Python Flask.</p>
    <a href="/">Back to Home</a>
    """

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
