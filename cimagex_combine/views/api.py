from flask import Blueprint, jsonify, send_file, abort, request
import cimagex_combine.api as api


api_blueprint = Blueprint('api_blueprint', __name__,
                  template_folder='templates',
                  static_folder='static')

@api_blueprint.route('/')
def test(user, endpoint):
	return jsonify('test')

@api_blueprint.route('/combine')
def combine():
	return jsonify(api.combine())