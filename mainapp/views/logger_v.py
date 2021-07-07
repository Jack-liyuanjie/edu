from flask import Blueprint, request, jsonify

blue = Blueprint('loggerBlue', __name__)


@blue.route('/log', methods=['POST'])
def upload_log():
    print(request.form)
    return jsonify({
        'msg': 'ok'
    })
