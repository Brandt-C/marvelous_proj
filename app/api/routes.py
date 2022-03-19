from flask import Blueprint, request, jsonify

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





