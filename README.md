# Beginner Starter Backend (Python + FastAPI)

A simple, clean Python backend API ready to deploy on [Render](https://render.com).

Perfect for learning how to build and deploy a real backend.

## Features

- FastAPI (modern, fast, automatic docs)
- Health check endpoint
- Simple in-memory Items CRUD
- Ready for Render (free tier friendly)
- Interactive API docs at `/docs`

## Project Structure

```
.
├── main.py              # The application
├── requirements.txt     # Dependencies
├── .gitignore
└── README.md
```

## Local Development

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# or
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at: **http://127.0.0.1:8000**

- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- Alternative docs (ReDoc): http://127.0.0.1:8000/redoc

### Quick test

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

## Deploy to Render (Free)

1. Push this project to a **GitHub** repository.
2. Go to [Render Dashboard](https://dashboard.render.com) → **New** → **Web Service**.
3. Connect your GitHub repo.
4. Configure the service:

   | Setting          | Value                                              |
   |------------------|----------------------------------------------------|
   | **Name**         | anything you like (e.g. `my-starter-backend`)      |
   | **Language**     | `Python 3`                                         |
   | **Build Command**| `pip install -r requirements.txt`                  |
   | **Start Command**| `uvicorn main:app --host 0.0.0.0 --port $PORT`     |

5. Choose the **Free** instance type.
6. Click **Create Web Service**.

Render will build and deploy your app.  
Once live, visit your `.onrender.com` URL + `/docs` to see the interactive documentation.

> **Note**: Free services on Render spin down after inactivity. The first request after idle may take a few seconds (cold start).

## API Endpoints

| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| GET    | `/`               | Welcome message            |
| GET    | `/health`         | Health check               |
| GET    | `/items`          | List all items             |
| POST   | `/items`          | Create a new item          |
| GET    | `/items/{id}`     | Get one item by ID         |
| DELETE | `/items/{id}`     | Delete an item             |

### Example: Create an item

```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "My first item", "description": "Learning backends is fun"}'
```

## Next Steps for Learning

1. Replace the in-memory list with a real database (SQLite → PostgreSQL).
2. Add authentication (JWT or OAuth).
3. Add environment variables (`.env` + `python-dotenv`).
4. Write tests with `pytest`.
5. Add CORS if you build a frontend.

## License

Free to use and modify for learning and personal projects.
