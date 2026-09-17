from flask import Flask, request, redirect

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return f"""
        <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <link rel="icon" href="data:,">
                <title>game codes</title>
            </head>
            <body>
                <div style="position:absolute;left:50%;top:50%;translate:-50% -50%;">
                    <form method="post" action="/post">
                        <input name="message" placeholder="code" required>
                        <button type="submit">Post</button>
                    </form>
                    <h2>Codes</h2>
                    {''.join('<p>' + msg + '</p>' for msg in messages)}
                    <a href="/delete">delete</a>
                    <a href="https://pvl.pythonanywhere.com" style="position:absolute;bottom:1vh;right:1vw;">Change host</a>
                </div>
            </body>
        </html>
"""

@app.route("/post", methods=["POST"])
def post():
    msg = request.form.get("message", "").strip()
    if msg:
        messages.append(msg.replace('<', '&lt;').replace('>', '&gt;'))
    return redirect("/")

@app.route("/delete", methods=["GET"])
def delete():
    global messages
    messages = []
    return redirect("/")
