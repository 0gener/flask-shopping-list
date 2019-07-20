from application import db
from sqlalchemy.orm import relationship

class GroupModel(db.Model):
    __tablename__ = 't_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    users = relationship("UserModel", secondary="t_user_has_t_group")
    items = relationship("ItemModel", back_populates="group")

    def __init__(self, name, created_at=None):
        self.name = name
        self.created_at = created_at

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
