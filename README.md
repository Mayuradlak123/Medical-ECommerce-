Medstore
===

Medstore is a Medical store alike website, built as the submission for the Minor project in the college.

## How to run Locally

- Clone this repository
    ```bash
    git clone https://github.com/Mayuradlak123/Medical-ECommerce-.git
    ```

- Alternatively you can [download](https://github.com/Mayuradlak123/Medical-ECommerce/archive/master.zip) this repository as `zip`, and extract it.
- Switch to the project directory and create a <span title="To access admin panel">superuser</span>
    ```bash
    cd medstore
    python3 manage.py createsuperuser
    ```
    <div style="border: 3px ridge #f44; padding: 2px 5px;">
    <strong>Note</strong>: Depending on the system, python3 above should be replaced by <code>python</code> or <code>py</code>(in windows)
    </div>

- Initialize database
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

- Run the server
  ```bash
  python3 manage.py runserver
  ```
  This will start a local server on `port 8000`.
- Open http://localhost:8000 or http://127.0.0.1:8000, in the browser to view the website

