import ffmpeg
import threading
import time
import subprocess
import numpy as np

from ui_form import Ui_Widget
from PySide6.QtWidgets import QWidget

from src.tools import DebugEmitter


input_options = {
    "loglevel": "info",
    "fflags": "nobuffer",
    "flags": "low_delay"
}

TIME_OUT = 1

class Streamer(QWidget):
    def __init__(self, parent=None, stream_size=(640, 480)):
        super().__init__(parent)

        self.ffmpeg_process = None
        self.current_frame = np.zeros((stream_size[1], stream_size[0], 3), dtype=np.uint8)
        self.stream_thread = None
        self.err_thread = None

        self.stream_width = stream_size[0]
        self.stream_height = stream_size[1]
        self.stream_lock = threading.Lock()

        self.debug = DebugEmitter(self)


    def start(self, url: str) -> None:
        self.ffmpeg_process = (
            ffmpeg
            .input(url, **input_options)
            .output('pipe:', format='rawvideo', pix_fmt='rgb24')
            .run_async(pipe_stdout=True, pipe_stderr=True)
        )
        self.stream_thread = threading.Thread(target=self.read_stream, daemon=True)
        self.stream_thread.start()
        self.err_thread = threading.Thread(target=self.monitor_stderr, daemon=True)
        self.err_thread.start()


    def stop(self) -> None:
        if self.ffmpeg_process:
            self.ffmpeg_process.terminate()  # или kill()
            self.ffmpeg_process.stdout.close()
            self.ffmpeg_process.stderr.close()
            self.ffmpeg_process.wait()
            self.ffmpeg_process = None


    def monitor_stderr(self) -> None:
        try:
            while True:
                line = self.ffmpeg_process.stderr.readline()
                if not line:
                    self.debug.send("stderr: EOF reached")
                    break
                self.debug.send(f"stderr: {line.decode().strip()}")
            self.debug.send("stderr thread stopped")
        except Exception as e:
            self.debug.send(f"Monitoring stderr was failed: {e}")



    def read_stream(self) -> None:
        while True:
            try:
                if self.ffmpeg_process:
                    data_size = self.stream_width * self.stream_height * 3
                    raw_frame = self.ffmpeg_process.stdout.read(data_size)

                    if raw_frame is None or len(raw_frame) != data_size:
                        print("Raw frame is empty or broken, sleeping...")
                        time.sleep(TIME_OUT)

                    with self.stream_lock:
                        self.current_frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape(
                            [self.stream_height, self.stream_width, 3])
                else:
                    time.sleep(0.1)
            except subprocess.SubprocessError as e:
                print(f"Subprocess error: {e}")
                time.sleep(TIME_OUT)
            except ValueError as e:
                print(f"ValueError error: {e}")


    def get_current_frame(self) -> np.ndarray:
        with self.stream_lock:
            return self.current_frame


