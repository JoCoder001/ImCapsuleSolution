from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from models import Recipe

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_data = {
            'id': recipe.id,
            'title': recipe.title,
            'description': recipe.description,
            'user_id': recipe.user_id
        }
        recipe_list.append(recipe_data)
    return jsonify(recipes=recipe_list), 200

@app.route('/recipes', methods=['POST'])
@jwt_required
def create_recipe():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify(message='Title and description are required.'), 400

    current_user = get_jwt_identity()

    new_recipe = Recipe(title=title, description=description, user_id=current_user)
    db.session.add(new_recipe)
    db.session.commit()

    return jsonify(message='Recipe created successfully.'), 201

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify(message='Recipe not found.'), 404

    recipe_data = {
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'user_id': recipe.user_id
    }
    return jsonify(recipe=recipe_data), 200

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required
def update_recipe(recipe_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify(message='Title and description are required.'), 400

    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify(message='Recipe not found.'), 404

    current_user = get_jwt_identity()

    if recipe.user_id != current_user:
        return jsonify(message='You are not authorized to update this recipe.'), 403

    recipe.title = title
    recipe.description = description
    db.session.commit()

    return jsonify(message='Recipe updated successfully.'), 200

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify(message='Recipe not found.'), 404

    current_user = get_jwt_identity()

    if recipe.user_id != current_user:
        return jsonify(message='You are not authorized to delete this recipe.'), 403

    db.session.delete(recipe)
    db.session.commit()

    return jsonify(message='Recipe deleted successfully.'), 200
