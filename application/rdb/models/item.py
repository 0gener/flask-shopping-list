from application import db
from sqlalchemy.orm import relationship

class ItemModel(db.Model):
    __tablename__ = 't_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    t_group_id = db.Column(db.Integer, db.ForeignKey('t_group.id'), nullable=False)
    t_user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'), nullable=False)
    cleared = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    counter = db.Column(db.Integer, nullable=False)

    group = relationship("GroupModel", back_populates="items")
    user = relationship("UserModel")

    def __init__(self, name, t_group_id, t_user_id):
        self.name = name
        self.t_group_id = t_group_id
        self.t_user_id = t_user_id

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name_and_group(cls, name, group_id):
        return cls.query.filter_by(name=name, t_group_id=group_id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
