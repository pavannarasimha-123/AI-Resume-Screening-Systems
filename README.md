# 🤖 AI Resume Screening System

An AI-powered Resume Screening System built using **FastAPI**, **PostgreSQL**, **FAISS**, and **Sentence Transformers**. The system automatically parses resumes, extracts skills, ranks candidates based on job descriptions, generates AI summaries, and provides an interactive dashboard for recruiters.

---

# 🚀 Features

- 🔐 JWT Authentication (Register/Login)
- 📄 Resume Upload (PDF)
- 📖 Automatic PDF Text Extraction
- 🗄️ PostgreSQL Database Integration
- 🧠 AI Resume Ranking using Sentence Transformers
- 🔍 Semantic Search using FAISS
- 🎯 Skill Matching
- 📊 Recruiter Dashboard
- 📝 AI Candidate Summary
- 📤 Export Candidate Results
- 📚 Interactive Swagger API Documentation

---

# 🏗️ System Architecture

```
               Resume Upload
                      │
                      ▼
              FastAPI Backend
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
 PostgreSQL Database          PDF Parser
         │
         ▼
 Resume Text Storage
         │
         ▼
 Sentence Transformer
         │
         ▼
 Resume Embeddings
         │
         ▼
      FAISS Index
         │
         ▼
 AI Candidate Ranking
         │
         ▼
 Dashboard & Candidate Summary
```

---

# 🛠️ Technology Stack

### Backend

- FastAPI
- Python
- SQLAlchemy
- Alembic
- JWT Authentication

### Database

- PostgreSQL

### AI / Machine Learning

- Sentence Transformers
- FAISS
- Scikit-Learn
- NumPy

### Document Processing

- PyMuPDF

### Deployment

- Docker
- Render

---

# 📂 Project Structure

```
AI-Resume-Screening-System/
│
├── app/
│   ├── routers/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── utils/
│   ├── core/
│   └── main.py
│
├── alembic/
├── uploads/
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql+psycopg2://username:password@host/database
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Migration

```bash
alembic upgrade head
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

After starting the server:

```
http://localhost:8000/docs
```

Swagger UI provides complete API documentation.

---

# 🤖 AI Workflow

1. Upload Resume (PDF)
2. Extract Resume Text
3. Generate Sentence Embeddings
4. Store Resume in PostgreSQL
5. Build FAISS Index
6. Compare Resume with Job Description
7. Calculate Similarity Score
8. Perform Skill Matching
9. Generate Candidate Summary
10. Display Ranked Candidates

---

# 📊 Ranking Parameters

The ranking score is based on:

- Semantic Similarity
- Skill Matching
- Missing Skills
- Candidate Recommendation

Recommendations:

- ⭐ Highly Recommended
- ✅ Recommended
- ⚠️ Needs Review

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t ai-resume-screening .
```

Run Container

```bash
docker run -p 8000:8000 ai-resume-screening
```

---

# ☁️ Deployment

The project is designed for deployment using **Docker** and **Render**.

### Note

The complete AI version uses:

- Sentence Transformers
- PyTorch
- FAISS

These libraries require more memory than the **Render Free (512 MB RAM)** instance provides.

For production deployments, two architectures are recommended:

1. **Single-Service Deployment** (Recommended for servers with sufficient RAM)
   - FastAPI
   - PostgreSQL
   - Sentence Transformers
   - FAISS

2. **Split Architecture** (Recommended for low-memory environments)
   - FastAPI handles authentication, resume uploads, dashboards, and APIs.
   - AI embedding generation and FAISS indexing run as a separate offline worker or service.
   - The web service consumes the precomputed embeddings and search index.

This separation reduces memory usage while preserving the AI functionality.

---

# Future Enhancements

- Email Notifications
- Resume Versioning
- OCR Support for Scanned PDFs
- AI Interview Question Generation
- Multi-language Resume Support
- Cloud Storage Integration
- Recruiter Analytics Dashboard

---
# 👨‍💻 Author

## Pavan Rajaboyina

**B.Tech Student**

Passionate about **Artificial Intelligence, Machine Learning, Full Stack Development, and Backend Engineering**. I enjoy building production-ready applications using FastAPI, Java, Python, PostgreSQL, and AI technologies.

### GitHub

https://github.com/pavannarasimha-123

### LinkedIn

https://www.linkedin.com/in/pavanrajaboyina

---

⭐ If you found this project useful, please consider giving it a **Star** on GitHub.


This project is developed for educational and portfolio purposes.
