# Pizza-Reeurant Flask API
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Data Models](#data-models)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Pizza Restaurant Flask API is a RESTful API built using Flask that allows you to manage and interact with a database of pizza restaurants, pizzas, and their relationships. It provides various endpoints for creating, retrieving, updating, and deleting restaurant and pizza data.

## Features

- Retrieve a list of all restaurants.
- Retrieve detailed information about a specific restaurant by ID.
- Delete a restaurant by ID, along with its associated data.
- Retrieve a list of all pizzas.
- Create a new restaurant-pizza relationship.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Pip package manager installed.
- SQLite or another compatible database installed (for storing data).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pizza-restaurant-flask-api.git
   ```

2. Navigate to the project directory:


3. Create a virtual environment (optional but recommended):

4. Activate the virtual environment:


5. Install the required dependencies:


## Usage

To run the Flask API, use the following command:

```bash
python run.py
```

The API will be accessible at `http://localhost:5555` by default.

## Endpoints

The API provides the following endpoints:

- `GET /`: Welcome message.
- `GET /restaurants`: Retrieve a list of all restaurants.
- `GET /restaurants/<int:id>`: Retrieve detailed information about a restaurant by ID.
- `DELETE /restaurants/<int:id>`: Delete a restaurant by ID.
- `GET /pizzas`: Retrieve a list of all pizzas.
- `POST /restaurant_pizzas`: Create a new restaurant-pizza relationship.

## Data Models

The API uses the following data models:

- `Restaurant`: Represents a pizza restaurant.
- `Pizza`: Represents a type of pizza.
- `RestaurantPizza`: Represents the relationship between a restaurant and a pizza.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Test your changes thoroughly.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License Mwaniki-Titus