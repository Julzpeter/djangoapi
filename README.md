# Backend Api
This is a public API that returns basic information in JSON format; including email, current datetime, and Github repository

## Setup Instructions

1. Clone the repository :
```bash
  git clone https://github.com/Julzpeter/djangoapi.git
```
- **cd your-repo**

2. Create virtual environment :

- **On macOS/Linux**:
python3 -m venv venv

- **On Windows**:
python3 -m venv venv

3. Activate the virtual environment:

- **On macOs/Linux**:
source venv/bin/activate

- **On Windows**:
venv Scripts/activate

4. Install dependencies :
pip3 install -r requirements.txt

5. Run the project:
python3 manage.py runserver

## API Documentation

1. Endpoint
- **URL**: `GET /api/  `
- **Description**: Returns email, current datetime and github url

2. Request
- **Method**: `GET`
- **URL**: `https://your-app-url/api/`

3. Response
- **Status Code**: `200 OK`
- **Response Format**: JSON
- **Example Response**:
    ```json
    {
        "email": "your-email@example.com",
        "current_datetime": "2025-01-30T09:30:00Z",
        "github_url":"https://github.comyourusernameyour-repo" 
    }

## Backlinks

Looking to hire a dev?
[PYTHON](https://hng.tech/hire/python-developers)
