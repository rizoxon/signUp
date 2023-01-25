from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template('index.html', TITLE="Home", MAIN="Home page")
@app.route("/signUp", methods=["GET", "POST"])
def signUp():
    if request.method == "GET":
        dom ="""
        <form>
            <input type="text" name="username" placeholder="Name">
            <input type="email" name="email" placeholder="Email">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" name="signUp" value="Sign Up">
        </form>
        """
        return render_template('index.html', TITLE="Sign Up", MAIN=dom)

    elif request.method == "POST":
        if len(request.get_json()["username"]) < 6:
            return make_response(json.dumps({
                "response": "error",
                "message": "Username must be at least 6 chars long!"
            }), 200)
        elif len(request.get_json()["password"]) < 6:
            return make_response(json.dumps({
                "response": "error",
                "message": "Password must be at least 6 chars long!"
            }), 200)
        else:
            return make_response(json.dumps({"response": "OK"}), 200)


if __name__ == "__main__":
    app.run(debug=True)