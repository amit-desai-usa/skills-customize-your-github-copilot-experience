# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints for reading and managing data, practicing request validation, and structuring a clean API workflow.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and create a health-check endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Import `FastAPI` from `fastapi`
- Create an app instance named `app`
- Add a `GET /health` endpoint
- Return a JSON response such as `{"status": "ok"}`

### 🛠️ Build a Resource Endpoint

#### Description
Create endpoints to manage a collection of items, such as books, tasks, or to-do entries.

#### Requirements
Completed program should:

- Define a simple data model using Python classes or Pydantic
- Add a `GET /items` endpoint to return all items
- Add a `POST /items` endpoint to create a new item
- Return the created item in JSON format

### 🛠️ Add Detail Routes and Validation

#### Description
Extend the API with individual item routes and basic validation for request data.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` endpoint to fetch one item
- Handle missing items gracefully with a 404-style response
- Validate request data before storing or returning it
- Use clear JSON field names and readable API responses

### 🛠️ Improve the API Experience

#### Description
Polish the API by adding a small feature that makes it easier to use and understand.

#### Requirements
Completed program should:

- Include at least one optional enhancement such as filtering, updating an item, or deleting an item
- Keep the API easy to read and consistent in naming
- Demonstrate how the API responds to valid and invalid requests
