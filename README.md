# Jant.ai

This is a web application for College University that helps you find your ideal roommate based on compatibility. It uses an embedding model to match users based on their preferences and interests.

## Prerequisites

Before running the application, make sure you have completed the following steps:

1. Create a `.env` file in the repository root directory.
2. Define the `COHAI_API_TOKEN` variable in the `.env` file. This token is required to access the embedding model.

## Installation

To install the dependencies, follow these steps:

1. Make sure you have [Poetry](https://python-poetry.org/) installed on your system.
2. Open a terminal and navigate to the repository root directory.
3. Run the following command to create a virtual environment and install the dependencies:

```shell
poetry install
```

## Running the Application

To run the application, follow these steps:

1. Open a terminal and navigate to the repository root directory.
2. Run the following command:

```shell
streamlit run main.py
```

3. The application will start running and you can access it in your web browser at the provided URL.

## License

This project is licensed under the [MIT License](LICENSE).