
from flask import Flask

app = Flask(__name__) # root path

# Routing/Mapping (connect python function to webpage)
# Use @ decorator to wrap and modify behavior of a python function
@app.route('/') # connect a webpage (/ for root directory)
def index(): # if connecting to e.g. profile instead of root, use index profile
	return 'This is the homepage' # replace this with other nice website stuff


@app.route('/tuna')
def tuna():
	return '<h2> The tuna page! </h2>'

@app.route('/profile/<username>')
def profile(username):
	return '<h2> Hiya %s </h2>' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return '<h2> This is post %r </h2>' % post_id

if __name__ == "__main__":
	app.run(debug=True) # start the app (in debugging mode)
