import pyaudio
import socket

# IP address and port of the receiving computer
receiver_ip = '172.31.9.190'
receiver_port = 1234

# Audio parameters
sample_rate = 48000
frames_per_buffer = 4096

# Create a UDP socket for sending audio data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream for capturing
capture_stream = audio.open(format=pyaudio.paInt16,
                            channels=2,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=frames_per_buffer,
                            output_device_index=-1)  # Set output_device_index to -1 to disable audio playback

# Start capturing and sending audio
while True:
    # Capture audio
    audio_data = capture_stream.read(frames_per_buffer, exception_on_overflow=False)

    # Send audio data over the network
    client_socket.sendto(audio_data, (receiver_ip, receiver_port))

# Close the stream and terminate PyAudio
capture_stream.stop_stream()
capture_stream.close()
audio.terminate()
client_socket.close()
