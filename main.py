from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/crud_family_tree'
db = SQLAlchemy(app)
ma = Marshmallow()


class Orang(db.Model):
    __tablename__ = "families"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    jenis_kelamin = db.Column(db.String(20))
    parent_id = db.Column(db.Integer, nullable=True)
    child_of = db.Column(db.Integer, nullable=True)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, nama, jenis_kelamin, parent_id, child_of):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.parent_id = parent_id
        self.child_of = child_of

    def __repr__(self):
        return f"{self.id}"


class Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orang
        load_instance = True

    id = fields.Number(dump_only=True)
    nama = fields.String(required=True)
    jenis_kelamin = fields.String(required=True)
    parent_id = fields.Integer(required=False, bool=False)
    child_of = fields.Integer(required=False, bool=False)


db.create_all()


@app.route('/', methods=['GET'])
def index():
    data = Orang.query.all()
    model_schema = Schema(many=True)
    result = model_schema.dump(data)
    return make_response(jsonify({"result": result}))


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    data = Orang(
        nama=data['nama'],
        jenis_kelamin=data['jenis_kelamin'],
        parent_id=data['parent_id'],
        child_of=data['child_of']
    )

    db.session.add(data)
    db.session.commit()
    return make_response(jsonify({"result": "Sukses"}), 200)


@app.route('/update', methods=['PUT'])
def update(id):
    data = request.get_json()
    id = Orang.query.get(id)
    if data.get('nama'):
        id.nama = data['nama']
    if data.get('jenis_kelamin'):
        id.jenis_kelamin = data['jenis_kelamin']
    if data.get('parent_id'):
        id.parent_id = data['parent_id']
    if data.get('child_of'):
        id.child_of = data['child_of']
    db.session.add(id)
    db.session.commit()
    return make_response(jsonify({"result": "updated"}), 200)


@app.route('/delete', methods=['GET'])
def delete(id):
    id = request.get_json()['id']
    data = Orang.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response(jsonify({"result": "deleted"}), 200)

@app.route('/visualize', methods=['GET'])
def visualize():
    tree_data = []
    dict_gender = {'Pria': 'man', 'Wanita': 'woman'}
    data = Orang.query.all()
    model_schema = Schema(many=True)
    result = model_schema.dump(data)
    for i, x in enumerate(result):
        if x['child_of'] is None:
            tree_data.append(
                {'name': x['nama'],
                 'class': dict_gender[x['jenis_kelamin']],
                 'parent_id': x['parent_id'],
                 'child_of': x['child_of'],
                 'children': []
                 }
            )
        if x['child_of'] is not None:
            if x['child_of'] == 0:
                tree_data[0]['children'].append({
                    'name': x['nama'],
                    'class': dict_gender[x['jenis_kelamin']],
                    'parent_id': x['parent_id'],
                    'child_of': x['child_of'],
                    'children': []
                })

    for i, x in enumerate(tree_data[0]['children']):
        for v in result:
            if v['child_of'] == x['parent_id']:
                x['children'].append(
                    {
                        'name': v['nama'],
                        'class': dict_gender[v['jenis_kelamin']],
                        'parent_id': v['parent_id'],
                        'child_of': v['child_of'],
                        'children': []
                    }
                )

    return make_response(jsonify({"result": tree_data}), 200)


if __name__ == '__main__':
    app.run(debug=True)
