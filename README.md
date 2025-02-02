# Todo API

## Project Description
The Todo API is a simple and efficient API for managing a todo list. It allows users to create, read, update, and delete tasks.

## Installation
To install the Todo API, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo_api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd todo_api
    ```
3. Install Poetry if you haven't already:
    ```sh
    pip install poetry
    ```
4. Install the dependencies:
    ```sh
    poetry install
    ```

## Usage
To start the server, run:
```sh
poetry run python -m todo_api
```

The API will be available at `http://localhost:3000`.

### Endpoints
- `GET /todos` - Retrieve all todos
- `POST /todos` - Create a new todo
- `GET /todos/:id` - Retrieve a specific todo by ID
- `PUT /todos/:id` - Update a specific todo by ID
- `DELETE /todos/:id` - Delete a specific todo by ID

## License
This project is licensed under the MIT License.
