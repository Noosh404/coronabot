from flask import jsonify

from corona.app import app
from corona.models.corona import Corona


@app.route('/corona/', methods=['GET'])
def get_all_corona():
    data = []
    for corona in Corona.objects.all():
        data.append(corona.to_dict())
    return jsonify(data), 200

@app.route('/corona/<corona_id>/', methods=['GET'])
def get_corona(corona_id):
    corona = Corona.object.raw({"_id": corona_id})
    if len(corona) == 1:
        corona = corona[0]
    else:
        return jsonify({"error": "Corona object not found"}), 404
    return jsonify(corona.to_dict()), 200
