from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    if request.method == 'POST':
        return 'Esto es un POST'
    else:
        return 'Hello!' 

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/usuario/<username>')
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run()
