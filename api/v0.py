from flask import flash, request, Blueprint, abort, jsonify
from models import Marker

api = Blueprint('api_v0', __name__, template_folder='templates')

@api.route('/markers')
def get_all_jobs():
    all_markers = Marker.query.filter(Marker.valid == 1).all()
    return jsonify(jobs=[m.serialize() for m in all_markers])

@api.route('/markers/<id>')
def get_job(id):
    marker = Marker.query.get(id)
    if marker:
        return jsonify(marker.serialize())
    else:
        return jsonify({'error': 'No marker with id {0}.'.format(id)}), 404
