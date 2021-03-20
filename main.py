from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
app = Flask(__name__)

print(response.status_code)
api_data = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=api_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/blogpost/<int:id>')
def get_blog(id):
    article = ""
    for post in api_data:
        if id == post['id']:
            article = post
    return render_template("post.html", post=article)


if __name__ == "__main__":
    app.run(debug=True)