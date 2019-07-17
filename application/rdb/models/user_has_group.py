from application import db
from sqlalchemy.orm import relationship, backref

class UserHasGroupModel(db.Model):
    __tablename__ = 't_user_has_t_group'

    id = db.Column(db.Integer, primary_key=True)
    t_user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'))
    t_group_id = db.Column(db.Integer, db.ForeignKey('t_group.id'))
    status = db.Column(db.String(45), nullable=False)
    invited_at = db.Column(db.DateTime, nullable=True)
    joined_at = db.Column(db.DateTime, nullable=True)
    is_owner = db.Column(db.Boolean, nullable=False)

    user = relationship("UserModel", foreign_keys=[t_user_id], backref=backref("t_user_has_t_group"))
    group = relationship("GroupModel", backref=backref("t_user_has_t_group"))

    def __init__(self, user, group):
        self.user = user
        self.group = group

    def save(self):
        db.session.add(self)
        db.session.commit()