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
                "category_name": category.name
            })

        return category_list

    def post(self):
        category_addition = request.get_json()
        category_details = MovieCategory.query.filter_by(
            category_name=category_addition['category_name']
            )

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
            category_name=category['category_name'].lower()).first()

        if category_details:
            category_details.category_name = category['username']
            category_details.save()
            
            return {"response": "Category updated successfully!"}, 201


    def delete(self):
        category_name = request.args.get('name')
        
        selected_category = MovieCategory.query.filter_by(
                    category_name=category_name).first()

        name = selected_category.category_name

        selected_category.delete()

        return {"response": "Category deleted",
                "Category that has been deleted": name}, 200
