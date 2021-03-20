from flask import Flask, render_template, request
import requests
import smtplib

response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
app = Flask(__name__)

MY_EMAIL = "---------------------------"
MY_PASSWORD = "----------------------"

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


@app.route('/blogpost/<int:index>')
def get_blog(index):
    article = ""
    for post in api_data:
        if index == post['id']:
            article = post
    return render_template("post.html", post=article)


@app.route('/form-entry', methods=["POST"])
def data_received():
    data = request.form
    send_email(data["name"], data["email"], data["phone"], data["message"])
    return render_template("form-entry.html")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)