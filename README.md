## Payment Processing System
This repository contains a simple payment processing system implemented in Python. It is built to be modular and allow the addition of payment processors easily.

## Running Locally
1. Clone the repository:
   ```bash
   git clone git@github.com:kibelenny/payment_process.git
    cd payment_process
    ```
2. Create a virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Access the application at `http://localhost:8000/api/v1/payments`.
7. Swagger documentation is available at `http://localhost:8000/api/schema/swagger-ui/`.

### Running Tests
To run the tests, use the following command:
    ```bash
    python manage.py test
    ```

## Deployment
The application is deployed in Render. You can view it [here](https://payment-process-gx0i.onrender.com/api/v1/payments).  
### Steps to deploy:
1. Create a render account and link your GitHub repository.
2. Create a new web service and select the repository.
3. Set the following commands:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python manage.py runserver 0.0.0.0:8000`
4. Set auto-deploy to off. Take note of the service ID and Render key in deploy hook provided.
5. In the GitHub repository, add the following secrets to enable automatic deployment:
   - `RENDER_SERVICE_ID`: Your Render service ID.
   - `RENDER_API_KEY`: Your Render key.
6. Push to the main branch to trigger tests and deployment.