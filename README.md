
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

```plaintext
librify
├── backend
│   ├── app
│   │   ├── main.py          # FastAPI entrypoint
│   │   ├── routers          # API route definitions
│   │   ├── models           # Database models
│   │   ├── schemas          # Pydantic schemas
│   │   ├── services         # Business logic
│   │   ├── utils            # Helper functions
│   │   └── config           # Configurations (DB, env, etc.)
│   ├── tests                # Backend tests
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Backend container setup
│
├── frontend
│   ├── pages                # Next.js pages
│   ├── components           # UI components
│   ├── styles               # Styling
│   ├── utils                # Frontend utils
│   ├── package.json         # Node.js dependencies
│   └── tsconfig.json        # TypeScript configuration
│
├── docker-compose.yml       # Orchestration for backend, frontend & Postgres
├── README.md                # Project documentation
└── .gitignore               # Ignore unnecessary files
```
---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/librify.git
cd librify
```

### 2. Configure environment variables
Create a `.env` file inside `backend/` with the database connection string:
```bash
cp backend/env.example backend/.env
```
Feel free to edit the values to match your local database credentials.

### 3. One-command helpers (Makefile)
Common tasks now have shortcuts:
```bash
make help          # list available commands
make db-up         # start postgres via docker compose
make backend-install
make migrate       # run alembic migrations
make backend-run   # start FastAPI with uvicorn
```

### 4. End-to-end backend setup
```bash
make db-up
make backend-install
make migrate
make backend-run
```

### 5. Frontend setup (Next JS) *if/when available*
```bash
cd frontend
npm install
npm run dev
```

---

## 🗂 Database migrations

- Migrations live under `backend/alembic`.
- Apply outstanding migrations: `make migrate`.
- Generate a new migration after editing SQLAlchemy models: `make revision message="add new column"`.
- The FastAPI app now relies on migrations instead of calling `Base.metadata.create_all`, so always run `make migrate` after pulling new changes.



