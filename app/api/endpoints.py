import os
from flask import request, jsonify, current_app
from app.parsers import parse_file
from app.models import ParsedData
from app.db import db
from app.api import api_blueprint

@api_blueprint.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided."}), 400

    filename = file.filename
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(filepath)

    try:
        content = parse_file(filepath)
        parsed_data = ParsedData(
            file_name=filename,
            content=content,
            file_type=filename.split('.')[-1],
            filepath=filepath
        )
        db.session.add(parsed_data)
        db.session.commit()
        return jsonify({"message": "File uploaded and parsed.", "content": content}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
