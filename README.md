# MongoBD API Example

## Abstract
For educational purposes only, use with caution.
This code base is intended to be a simple example of a MongoDB API. 
Production environments may have additional concerns that are not addressed here.

## Tech Stack
- Python3: `python3.10`
- FastAPI: `fastapi`
- MongoDB: `pymongo[srv]`
- Uvicorn: `uvicorn[standard]`

## Git Flow
1. Clone the repo: `git clone <repo-url>`
2. Setup your local development environment (see below)
3. Create a feature branch: `git checkout -b feature/<your-feature>`
4. Make Changes: add features etc.
5. Push your branch: `git push origin feature/<your-feature>`

## Installation and Setup
1. Create local virtual environment: `python -m venv venv`
2. Activate local virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run local development server: `uvicorn app.api:API --reload`
