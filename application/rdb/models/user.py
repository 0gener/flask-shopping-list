from application import db
from sqlalchemy.orm import relationship

class UserModel(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    groups = relationship("GroupModel", secondary="t_user_has_t_group")

    def __init__(self, username, password, first_name, last_name, email, created_at=None):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "lat_name": self.last_name,
            "email": self.email,
            "created_at": self.created_at
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
