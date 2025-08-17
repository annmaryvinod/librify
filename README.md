
# 📚 Librify

Librify is a simple full-stack web app to keep track of the books you’ve read.  
It allows you to store book details such as **title, author, and language**.  

The stack:
- **Frontend**: Next.js (TypeScript)
- **Backend**: FastAPI
- **Database**: PostgreSQL (via Docker)
- **Deployment**: Docker Compose (planned)

---

## 🚀 Project Structure

librify/
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── models.py # SQLAlchemy models
│ │ ├── schemas.py # Pydantic schemas
│ │ ├── crud.py # DB operations
│ │ ├── database.py # DB connection setup
│ │ └── routers/ # API routes
│ │ └── books.py
│ ├── requirements.txt # Python dependencies
│ └── Dockerfile # Backend Dockerfile
│
├── frontend/ # Next.js frontend
│ ├── pages/
│ │ ├── index.tsx # Homepage UI
│ │ └── _app.tsx
│ ├── components/ # Reusable components
│ ├── package.json # Node dependencies
│ └── Dockerfile # Frontend Dockerfile
│
├── docker-compose.yml # Orchestrates services
├── README.md # Project documentation
└── .gitignore # Ignored files



---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/librify.git
cd librify
```

### 2. Run postgresql with Docker
```bash
docker run --name librify-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=librify -p 5432:5432 -d postgres
```

### 3. Backend setup (FastAPI)
```bash 
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Frontend setup (Next JS)
```bash
cd frontend
npm install
npm run dev
```



