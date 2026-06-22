from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    color = os.environ.get("APP_COLOR", "blue")

    return f"""
    <html>
    <body style="
        background-color:{color};
        display:flex;
        flex-direction: column;
        justify-content:center;
        align-items:center;
        height:100vh;
        margin:0;
        font-family:Arial;">
        <h1>Flask Color Application</h1>
        <h2>Current Color: {color}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
