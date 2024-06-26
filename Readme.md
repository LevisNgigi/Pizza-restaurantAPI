# Pizza Restaurant API

For this assessment, you'll be working with a Pizza Restaurant domain.

Your job is to build out the Flask API to add the functionality described in the deliverables below.

Test your endpoints as stated below

Running the Flask server and using Postman to make requests.

## Table of Contents
- [Setup](#setup)
- [Endpoints](#endpoints)
  - [Get All Restaurants](#get-all-restaurants)
  - [Get Restaurant by ID](#get-restaurant-by-id)
  - [Delete Restaurant](#delete-restaurant)
  - [Get All Pizzas](#get-all-pizzas)
  - [Create Restaurant Pizza](#create-restaurant-pizza)

## Setup

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/your-repo.git
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```
   python app.py
   ```

4. **Access the API:**
   - The API will be available at `http://localhost:5000`.

## Endpoints

### Get All Restaurants

- **URL:** `/restaurants`
- **Method:** `GET`
- **Description:** Retrieve a list of all restaurants.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Restaurant Name",
      "address": "Restaurant Address"
    },
    {
      "id": 2,
      "name": "Another Restaurant",
      "address": "Another Address"
    },
    ...
  ]
  ```

### Get Restaurant by ID

- **URL:** `/restaurants/<int:id>`
- **Method:** `GET`
- **Description:** Retrieve details of a specific restaurant by its ID.
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Restaurant Name",
    "address": "Restaurant Address",
    "pizza": [
      {
        "id": 1,
        "name": "Pizza Name",
        "ingredients": "List of Ingredients"
      },
      ...
    ]
  }
  ```

### Delete Restaurant

- **URL:** `/restaurants/<int:id>`
- **Method:** `DELETE`
- **Description:** Delete a restaurant by its ID.
- **Response:** No content, returns status code 204 on success.

### Get All Pizzas

- **URL:** `/pizzas`
- **Method:** `GET`
- **Description:** Retrieve a list of all pizzas.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Pizza Name",
      "ingredients": "List of Ingredients"
    },
    {
      "id": 2,
      "name": "Another Pizza",
      "ingredients": "Another List of Ingredients"
    },
    ...
  ]
  ```

### Create Restaurant Pizza

- **URL:** `/restaurant_pizzas`
- **Method:** `POST`
- **Description:** Create a new association between a restaurant and a pizza with pricing information.
- **Request Body:**
  ```json
  {
    "price": 10.99,
    "pizza_id": 1,
    "restaurant_id": 1
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Pizza Name",
    "ingredients": "List of Ingredients"
  }
  ```
- **Status Code:** 201 Created

## Author

- **Name:** Levis Ngigi

## License

This project is licensed under the MIT license.