from flask import Flask, render_template

app = Flask(__name__)

@app.route("/fail/<user>")
def main(user):
    return render_template('index.html', name = user)

if __name__ == "__main__":
    app.run()
