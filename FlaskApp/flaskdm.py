from flask import Flask

app = Flask(__name__)

@app.route("/") #decorators
def hello():
    return "Hello World" 

@app.route("/url2") #decorators
def new_url():
    return "Other URLL" 

app.route("/post/<int:post_id>", methods=["POST"])
def mostrar_post(post_id):
    return "Post %d" % post_id

if __name__ == '__main__':
    app.debug = True
    app.run()
