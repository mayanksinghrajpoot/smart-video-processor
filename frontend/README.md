# Smart Video Processor

A full-stack web application that allows users to upload videos and get back a processed version where:
- Silent parts are automatically skipped or accelerated
- Optionally, the entire video can be fast-forwarded at 2x speed
- Output maintains original quality

---

## 📁 Project Structure

```
smart-video-processor/
├── backend/                        # FastAPI backend
│   ├── main.py                     # FastAPI app and processing logic
│   ├── requirements.txt            # Backend dependencies
│   ├── uploads/                    # Temporarily stores uploaded videos
│   ├── processed/                  # Stores processed videos
│
├── frontend/                       # React + Vite + Tailwind frontend
│   └── (Your React app files...)
│
├── README.md                       # Project instructions
└── .gitignore
```

---

## 🚀 Features
- Upload video files (any format supported by FFmpeg)
- Choose whether to fast-forward the whole video
- Automatically removes silent gaps
- Download the processed video

---

## 🔧 Backend Setup (FastAPI)

### Prerequisites:
- Python 3.10+
- FFmpeg installed and available in your system PATH

### Installation:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Backend:
```bash
uvicorn main:app --reload
```

### API Endpoints:
- `POST /process` - Upload and process video
- `GET /download/{filename}` - Download processed video

---

## 🎨 Frontend Setup (React + Tailwind)

### Prerequisites:
- Node.js & npm

### Installation:
```bash
cd frontend
npm install
npm run dev
```

Update `fetch()` URLs to match your backend host (e.g., `http://localhost:8000/process`).

---

## 🌐 Deployment Guide

### Backend:
- Deploy `backend/` to [Railway](https://railway.app/) or [Render](https://render.com/)
- Add `FFmpeg` build support (Render supports FFmpeg natively, Railway may need Docker)

### Frontend:
- Deploy `frontend/` to [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/)

---

## ✅ To-Do
- [ ] Add progress indicator during upload/processing
- [ ] Drag-and-drop UI for upload
- [ ] Add user authentication (optional)



Built with ❤️ using FastAPI, FFmpeg, and React.
