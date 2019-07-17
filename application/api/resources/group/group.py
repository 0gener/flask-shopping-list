from application import db
from flask import request
from flask_restful import Resource
from application.api.resources.group.models.create_group_request import CreateGroupRequest
from flask_jwt_extended import jwt_required, get_jwt_identity
from application.rdb.models.group import GroupModel
from application.rdb.models.user import UserModel
from application.rdb.models.user_has_group import UserHasGroupModel
from application.rdb.models.enums.group_status import GroupStatus

class Group(Resource):
    @jwt_required
    def post(self):
        req = CreateGroupRequest(request.get_json())

        req.validate()

        group = GroupModel(req.name)

        current_user_id = get_jwt_identity()

        user = UserModel.find_by_id(current_user_id)

        user_group = UserHasGroupModel(user, group)

        user_group.status = GroupStatus.JOINED.value
        user_group.joined_at = db.func.current_timestamp()
        user_group.is_owner = True

        user_group.save()

        return {"message": "Group created successfully."}, 201