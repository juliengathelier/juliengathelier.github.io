from flask import Flask
app = Flask("François Hollande API")
@app.route("http://juliengathelier.github.io/")


def hello():
    
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
