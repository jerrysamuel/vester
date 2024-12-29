from app.db import db

class ParsedData(db.Model):
    __tablename__ = 'parsed_data'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
