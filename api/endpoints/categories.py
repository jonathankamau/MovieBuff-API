from flask import request
from flask_restplus import Resource
from api.utils import MovieCategory, token_required

class Categories(Resource):

    
    def get(self):
        categories = MovieCategory.query.all()
        category_list = []

        for category in categories:
            category_list.append({
                "category_id": category.id,
                "category_name": category.category_name
            })

        return category_list

    def post(self):
        category_addition = request.get_json()
        category_details = MovieCategory.query.filter_by(
            category_name=category_addition['category_name']
            ).first()

        if category_details:
            return {"message": "Category already exists!"}, 400
        else:
            new_category = MovieCategory(
                category_name=category_addition['category_name'].lower())
            
            new_category.save()

            return {"message": "Category saved successfully!"}, 201

    def put(self):
        category = request.get_json()

        category_details = MovieCategory.query.filter_by(
            category_name=category['old_category'].lower()).first()

        print(category_details)
        if category_details:
            category_details.category_name = category['new_category'].lower()
            category_details.save()
            
            return {"response": "Category updated successfully!"}, 201
        else:

            return {"response": "Could not update category!"}, 400

    def delete(self):
        category_name = request.get_json()
        
        selected_category = MovieCategory.query.filter_by(
                    category_name=category_name['category']).first()

        name = selected_category.category_name

        selected_category.delete()

        return {"response": "Category deleted",
                "Category that has been deleted": name}, 200
