from pydub import AudioSegment
from pydub.playback import play

# サンプリング周波数や音のパラメータを設定
fs = 44100
A = 0.5
f = 440
duration = 1000  # ミリ秒

# サイン波を生成
t = np.arange(0, duration / 1000, 1 / fs)
y = A * np.sin(2 * np.pi * f * t)

# サイン波をAudioSegmentに変換
audio = AudioSegment(y.tobytes(), frame_rate=fs, sample_width=y.dtype.itemsize, channels=1)

# サウンド再生
play(audio)

