# How to run : python video_ascii.py video.mp4 --audio on --subs on
import cv2
import os
import time
import shutil
import sys
import subprocess
import srt
import datetime

# ASCII characters (dark → light)
ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, term_cols, term_rows):
    """Convert a video frame to ASCII adjusted to terminal size."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize frame to terminal size
    resized = cv2.resize(gray, (term_cols, term_rows))

    ascii_frame = ""
    for row in resized:
        for pixel in row:
            ascii_frame += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
        ascii_frame += "\n"
    return ascii_frame

def load_subtitles(video_path):
    """Look for .srt file with the same name as the video"""
    base, _ = os.path.splitext(video_path)
    srt_file = base + ".srt"
    if os.path.exists(srt_file):
        with open(srt_file, "r", encoding="utf-8") as f:
            return list(srt.parse(f.read()))
    return []

def get_current_sub(subs, current_time):
    """Return subtitle text for current timestamp"""
    for sub in subs:
        if sub.start <= current_time <= sub.end:
            return sub.content
    return ""

def play_video_ascii(video_path, play_audio=False):
    subs = load_subtitles(video_path)

    # Start audio with ffplay if enabled
    audio_proc = None
    if play_audio:
        try:
            audio_proc = subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", video_path]
            )
        except FileNotFoundError:
            print("⚠ FFmpeg/ffplay not found. Install it from https://ffmpeg.org/")
            play_audio = False

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file '{video_path}'.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS) or 24
    delay = 1 / fps

    term_cols, term_rows = shutil.get_terminal_size(fallback=(80, 24))

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            current_time = datetime.timedelta(milliseconds=ms)

            ascii_frame = frame_to_ascii(frame, term_cols, term_rows - 2)  # leave 2 lines for subs

            # Add subtitle if available
            sub_text = get_current_sub(subs, current_time)
            if sub_text:
                ascii_frame += "\n" + (" " * max(0, (term_cols - len(sub_text)) // 2)) + sub_text

            # os.system('cls' if os.name == 'nt' else 'clear')
            # sys.stdout.write(ascii_frame)
            sys.stdout.write("\033[H" + ascii_frame)
            sys.stdout.flush()

            time.sleep(delay)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        if audio_proc:
            audio_proc.terminate()
        print("\nStopped.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python video_ascii.py <video_file> [audio=on|off] [subs=on|off]")
        sys.exit(1)

    video_file = sys.argv[1]
    audio_flag = any(arg.lower() == "--audio" or arg.lower() == "audio=on" for arg in sys.argv)
    subs_flag = any(arg.lower() == "--subs" or arg.lower() == "subs=on" for arg in sys.argv)

    play_video_ascii(video_file, play_audio=audio_flag)
