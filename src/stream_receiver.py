import ffmpeg
import threading
import time
import subprocess
import numpy as np

from PySide6.QtWidgets import QWidget

from src.tools import DebugEmitter


input_options = {
    "loglevel": "info",
    "fflags": "nobuffer",
    "fflags": "discardcorrupt",
    "flags": "low_delay",
    "pkt_size": 1316,
    "probesize": "100k"
}

TIME_OUT = 1


class StreamSize:
    SIZE_720 = (0, (960, 720))
    SIZE_480 = (1, (640, 480))
    SIZE_360 = (2, (480, 360))
    SIZE_240 = (3, (320, 240))
    SIZE_144 = (4, (192, 144))

class StreamReceiver(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ffmpeg_process = None

        self.stream_thread = None
        self.err_thread = None
        self.current_frame = np.zeros((128, 128, 3), dtype=np.uint8)
        self.stream_width = 0
        self.stream_height = 0
        self.stream_lock = threading.Lock()
        self.debug = DebugEmitter()

        self.set_stream_size(StreamSize.SIZE_720[1])


    def set_stream_size(self, res):
        self.current_frame = np.zeros((res[1], res[0], 3), dtype=np.uint8)
        self.stream_width = res[0]
        self.stream_height = res[1]
        self.debug.send(f"Stream resolution is set to {res}")


    def start(self, url: str) -> None:
        """
        Starts receiving ffmpeg stream on given url
        :param url:
        :return None:
        """
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
        """
        Stops the ffmpeg stream
        :return None:
        """
        if self.ffmpeg_process:
            self.ffmpeg_process.kill()
            self.ffmpeg_process = None


    def monitor_stderr(self) -> None:
        """
        Displays in debug window stderr messages
        :return None:
        """
        try:
            while self.ffmpeg_process is not None:
                line = self.ffmpeg_process.stderr.readline()
                if not line:
                    self.debug.send("stderr: EOF reached")
                    break
                self.debug.send(f"stderr: {line.decode().strip()}")
            self.debug.send("stderr thread stopped")
        except Exception as e:
            self.debug.send(f"Monitoring stderr was failed: {e}")


    def read_stream(self) -> None:
        """
        Reads the stream pipe than saving the current frame
        :return None:
        """
        if self.stream_width == 0 or self.stream_height == 0:
            self.debug.send("Stream size was not set, exiting...")
            self.stop()

        while True:
            try:
                if self.ffmpeg_process:
                    data_size = self.stream_width * self.stream_height * 3
                    raw_frame = self.ffmpeg_process.stdout.read(data_size)
                    self.ffmpeg_process.stdout.flush()

                    if raw_frame is None or len(raw_frame) != data_size:
                        self.debug.send("Raw frame is empty or broken, exiting...")
                        self.stop()
                        break

                    with self.stream_lock:
                        self.current_frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape(
                            [self.stream_height, self.stream_width, 3])
                else:
                    time.sleep(0.1)
            except subprocess.SubprocessError as e:
                self.debug.send(f"Subprocess error: {e}")
                time.sleep(TIME_OUT)
            except ValueError as e:
                self.debug.send(f"ValueError error: {e}")
            except Exception as e:
                print("Exiting read stream...")


    def get_current_frame(self) -> np.ndarray:
        """
        Gets the current frame
        :return:
        """
        with self.stream_lock:
            return self.current_frame


    def change_stream_size_with_index(self, index) -> None:
        if index == StreamSize.SIZE_720[0]:
            self.set_stream_size(StreamSize.SIZE_720[1])
        elif index == StreamSize.SIZE_480[0]:
            self.set_stream_size(StreamSize.SIZE_480[1])
        elif index == StreamSize.SIZE_360[0]:
            self.set_stream_size(StreamSize.SIZE_360[1])
        elif index == StreamSize.SIZE_240[0]:
            self.set_stream_size(StreamSize.SIZE_240[1])
        else:
            self.set_stream_size(StreamSize.SIZE_144[1])


    def get_stream_size(self) -> tuple[int, int]:
        return self.stream_width, self.stream_height
