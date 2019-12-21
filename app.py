from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__, static_url_path='')


client = MongoClient()
app.config['MONGO_URI'] = 'mongodb://localhost:27017/vintage'
app.config['SECRET_KEY'] = 'clown123'
mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def index():
    """Return homepage."""
    items = db['items'].find()
    return render_template('home.html', items=items)

@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/delete/<itemId>')
def playlists_delete(itemId):
    db['items'].delete_one({'_id': ObjectId(itemId)})
    return redirect('/')


@app.route('/new', methods=['POST'])
def post_new():
    item = {
        'name': request.form.get('name'),
        'image': request.form.get('url'),
        'price': request.form.get('price'),
        'description': request.form.get('description')
    }
    db['items'].insert_one(item)
    return redirect('/')


@app.route('/edit/<itemId>')
def edit(itemId):
    item = db['items'].find_one({ '_id': ObjectId(itemId) })
    return render_template('edit.html', item=item)

@app.route('/edit/<itemId>', methods=['POST'])
def edit_item(itemId):
    updated_item = {
        'name': request.form.get('name'),
        'image': request.form.get('url'),
        'price': request.form.get('price'),
        'description': request.form.get('description')
    }
    db['items'].update_one(
        {'_id': ObjectId(itemId)},
        {'$set': updated_item})
    return redirect('/')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True)
