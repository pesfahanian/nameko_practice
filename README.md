# nameko_practice

A simple micro-service application that uses [RabbitMQ](https://www.rabbitmq.com/) and `RPC` for communication.

This application is developed using:

-   [FastApi](https://fastapi.tiangolo.com/)
-   [nameko](https://github.com/onefinestay/nameko)
-   [SQLAlchemy](https://www.sqlalchemy.org/)

## Usage
Make sure you have a `RabbitMQ` server running locally.

-   Create a virtual environment:
    ```shell
    $ python -m venv .venv
    ```
-   Activate the virtual environment:
    ```shell
    $ source .venv/bin/activate
    ```
-   Install the required packages:
    ```shell
    $ pip install -r requirements.txt
    ```
-   Relocate to the `products` directory:
    ```shell
    $ cd products
    ```
-   Start the `nameko` service:
    ```shell
    $ nameko run main --backdoor 6060
    ```
-   Open a second terminal and relocate to the `gateway` directory:
    ```shell
    $ cd gateway
    ```
-   Start the `FastAPI` service:
    ```shell
    $ uvicorn main:app --reload
    ```
