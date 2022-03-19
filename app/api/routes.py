from flask import Blueprint, render_template, request, jsonify

api = Blueprint('api', __name__, url_prefix='/api')




from app.models import db, Char




        # self.s_name = dict['s_name'].title()
        # self.name = dict['name'].title()
        # self.description = dict['description']
        # self.comic_appearances = dict['comic_appearances']
        # self.super_power = dict['super_power']
        # self.equipment = dict['equipment']
        # self.contributor = dict['contributor']
@api.route('/add/character', methods=['POST'])
def add_char():
    try:
        data = request.get_json()
        n_char = Char(data)
        db.session.add(data)
        db.session.commit()
        return jsonify({'Thanks for adding a new character!': n_char.to_dict()}), 201
    except:
        return jsonify({'Nope. . .' : 'Either already exists or something went wrong!'}), 418

@api.route('/characters')
def getChars():
    chars = {'Char': [c.to_dict() for c in Char.query.all()]}
    return jsonify(chars), 200

@api.route('/character/<string:s_name>')
def getChar(s_name):
    c = Char.query.filter_by(s_name=s_name.title()).first()
    if c:
        return jsonify(c.to_dict()), 200
    else:
        return jsonify({'No dice':'No character found by that entry.'}), 418

@api.route('/character/update/<string:s_name>', methods=['PUT'])
def updateChar(s_name):
    try:
        char = Char.query.get(s_name)
        data = request.get_json()
        char.from_dict(data)
        db.session.commit()
        return jsonify({'Character updated': char.to_dict()})
    except:
        return jsonify({'No dice.': 'maybe it was you, maybe it was us but that didn\'t work.'})

@api.route('/character/del/<string:s_name>', methods=['DELETE'])
def delChar(s_name):
    char = Char.query.get(s_name)
    if not char:
        return jsonify({'Can\'t delete-': 'Not found or doesn\'t exist'}), 418
    db.session.delete(char)
    db.session.commit()
    return jsonify({'I hope you\'re happy. . . Deleted-': char.to_dict()}), 200

# @api.route('/add_char', methods=['GET', 'POST'])
# def guiAddChar():
#     return render_template('/add_char.html')

