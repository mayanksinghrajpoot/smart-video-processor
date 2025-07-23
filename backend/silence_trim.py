import subprocess

def process_video(input_path, output_path, fast_forward=False):
    if fast_forward:
        cmd = [
            "ffmpeg", "-i", input_path,
            "-filter_complex", "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]",
            "-map", "[v]", "-map", "[a]",
            "-crf", "18", "-preset", "ultrafast", output_path
        ]
    else:
        cmd = [
            "ffmpeg", "-i", input_path,
            "-af", "silenceremove=1:0:-50dB",
            "-crf", "18", "-preset", "ultrafast", output_path
        ]

    subprocess.run(cmd, check=True)

