from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    """Return homepage."""
    return render_template('home.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')
# OUR MOCK ARRAY OF PROJECTS
# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
# ]
#
# @app.route('/playlists')
# def playlists_index():
#     """Show all playlists."""
#     return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)
