# Recipe Management API
This is a Flask-based API for managing recipes. It provides endpoints to register and authenticate users, as well as perform CRUD operations on recipes.

## Features
- User registration and login with JWT authentication.
- Create, read, update, and delete recipes.
- Protected routes that require authentication.

## Installation
1. Clone the repository:
2. Change into the project directory:
3. Create a virtual environment:
4. Activate the virtual environment:
- For macOS/Linux:

  ```
  $ source venv/bin/activate
  ```

- For Windows:

  ```
  $ venv\Scripts\activate
  ```
5. Install the dependencies:
6. Set up the configuration:
- Rename the `config.py.example` file to `config.py`.
- Modify the configuration values in `config.py` as per your requirements.
7. Initialize the database:

2. The API will be accessible at `http://localhost:5000`.

## API Endpoints

- **POST /register**: Register a new user.
- **POST /login**: Authenticate a user and obtain an access token.
- **GET /protected**: Example protected route that requires authentication.
- **GET /recipes**: Get all recipes.
- **POST /recipes**: Create a new recipe.
- **GET /recipes/{recipe_id}**: Get a specific recipe.
- **PUT /recipes/{recipe_id}**: Update a specific recipe.
- **DELETE /recipes/{recipe_id}**: Delete a specific recipe.

Note: Replace `{recipe_id}` in the endpoint URLs with the actual ID of a recipe.

## Testing
To run the unit tests, execute the following command:

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.







