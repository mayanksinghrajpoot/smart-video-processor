# Smart Video Processor Backend (FastAPI)

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import uuid
import shutil
import subprocess

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
PROCESSED_DIR = "processed"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Utility to process the video (mock for now)
def process_video_ffmpeg(input_path: str, output_path: str, fast_forward: bool):
    if fast_forward:
        # Speed up entire video by 2x
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-filter_complex", "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]",
            "-map", "[v]", "-map", "[a]", output_path
        ]
    else:
        # Simulate silence removal (custom logic can be added here)
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-af", "silenceremove=start_periods=1:start_silence=0.3:start_threshold=-30dB",
            output_path
        ]
    subprocess.run(cmd, check=True)

@app.post("/process")
async def process_video(file: UploadFile = File(...), fast_forward: bool = False):
    file_ext = os.path.splitext(file.filename)[1]
    video_id = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_DIR, f"{video_id}{file_ext}")
    output_path = os.path.join(PROCESSED_DIR, f"{video_id}_processed.mp4")

    # Save the uploaded video
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the video
    process_video_ffmpeg(input_path, output_path, fast_forward)

    # Return processed file path
    return {"video_url": f"/download/{os.path.basename(output_path)}"}

@app.get("/download/{filename}")
def download_file(filename: str):
    return FileResponse(path=os.path.join(PROCESSED_DIR, filename), filename=filename, media_type='video/mp4')
