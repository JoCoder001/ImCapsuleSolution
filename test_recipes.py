import unittest
import json
from app import app, db
from models import User

class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.app.post('/register', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'User registered successfully.')

    def test_login(self):
        user = User(username='testuser')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.app.post('/login', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', data)

    def test_get_recipes(self):
        response = self.app.get('/recipes')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['recipes']), 0)

    def test_create_recipe(self):
        data = {
            'title': 'Test Recipe',
            'description': 'This is a test recipe'
        }
        response = self.app.post('/recipes', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Recipe created successfully.')

    def test_get_recipe(self):
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        db.session.add(recipe)
        db.session.commit()

        response = self.app.get(f'/recipes/{recipe.id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['recipe']['title'], 'Test Recipe')
        self.assertEqual(data['recipe']['description'], 'This is a test recipe')

    def test_update_recipe(self):
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        db.session.add(recipe)
        db.session.commit()

        data = {
            'title': 'Updated Recipe',
            'description': 'This is an updated recipe'
        }
        response = self.app.put(f'/recipes/{recipe.id}', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Recipe updated successfully.')

    def test_delete_recipe(self):
        recipe = Recipe(title='Test Recipe', description='This is a test recipe')
        db.session.add(recipe)
        db.session.commit()

        response = self.app.delete(f'/recipes/{recipe.id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Recipe deleted successfully.')

if __name__ == '__main__':
    unittest.main()
