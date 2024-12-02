
---

## **Features**

- **Inventory Management**: Add, update, and delete inventory items.
- **Order Management**: Place, Update, Delete and track orders.
- **RESTful APIs**: Built with Django Rest Framework.
- **PostgreSQL Database**: Connects to an RDS instance for persistent data storage.
- **Deployed on AWS**: Running on an EC2 instance with RDS integration.


---

## **Setup Instructions**

### **1. Prerequisites**

- Python 3.8 or higher
- PostgreSQL database
- Docker (optional for containerized deployment)

### **2. Installation**

1. Clone the repository:
   
   git clone https://github.com/7410abhi/django-ecommerce.git
   cd django-ecommerce

2. Create and activate a virtual environment:

    python3 -m venv ecommerce_env
    source ecommerce_env/bin/activate

3. Install dependencies:

    pip install -r requirements.txt

4. Run migrations to set up the database:

    python manage.py makemigrations
    python manage.py migrate

5. Run the development server:

    python manage.py runserver 



Inventory API Endpoints:

    Inventory
    1. List All Inventory Items

        curl --location 'http://35.90.122.137:8000/api/inventory/' \
        --header 'Content-Type: application/json'

    2. Create a New Inventory Item

    curl --location 'http://35.90.122.137:8000/api/inventory/' \
    --header 'Content-Type: application/json' \
    --data '{
    "name": "Product A",
    "stock": 50
    }'

    3. Update an Inventory Item

    curl --location --request PUT 'http://35.90.122.137:8000/api/inventory/1/' \
    --header 'Content-Type: application/json' \
    --data '{
    "name": "Product A Updated",
    "stock": 60
    }'

    4. Delete an Inventory Item

    curl --location --request DELETE 'http://35.90.122.137:8000/api/inventory/1/'


Orders API Endpoints:
    1. List All Orders

    curl --location 'http://35.90.122.137:8000/api/orders/' \
    --header 'Content-Type: application/json'

    2. Create a New Order
    
    curl --location 'http://35.90.122.137:8000/api/orders/' \
    --header 'Content-Type: application/json' \
    --data '{
    "user_id": 101,
    "status": "created"
    }'
    3. Update an Order

    
    curl --location --request PUT 'http://35.90.122.137:8000/api/orders/1/' \
    --header 'Content-Type: application/json' \
    --data '{
    "status": "shipped"
    }'

    4. Delete an Order
    
    curl --location --request DELETE 'http://35.90.122.137:8000/api/orders/1/'


Note: You can find the dummy data inngestion command in sql_scipts. 
