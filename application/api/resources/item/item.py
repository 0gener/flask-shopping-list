from application import db
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from application.rdb.models.item import ItemModel
from .models.create_item_request import CreateItemRequest
from application.rdb.models.group import GroupModel

class Item(Resource):
    @jwt_required
    def post(self, group_id):
        req = CreateItemRequest(request.get_json())

        req.validate()

        group = GroupModel.find_by_id(group_id)

        if not group:
            return {"message": "Group doesn't exist"}, 404

        item = ItemModel.find_by_name_and_group(req.name, group_id)

        if item:
            item.counter += 1
        else:
            current_user_id = get_jwt_identity()

            item = ItemModel(req.name, group_id, current_user_id)

            item.counter = 1

        item.cleared = False

        item.save()

        return {"message": "Item created"}, 201