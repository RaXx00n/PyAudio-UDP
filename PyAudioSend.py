import pyaudio
import socket

# IP address and port of the receiving computer
receiver_ip = '172.31.9.190'
receiver_port = 1138

# Audio parameters
sample_rate = 48000  # Increased sample rate to 48000 Hz
frames_per_buffer = 4096  # Increased buffer size to 4096 frames

# Create a UDP socket for sending audio data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Find the index of the line-in/microphone input device
input_device_index = None
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    if device_info['name'].startswith('Line In') or device_info['name'].startswith('Microphone'):
        input_device_index = i
        break

# Open the audio stream for capturing from the line-in/microphone input
capture_stream = audio.open(format=pyaudio.paInt16,
                            channels=2,
                            rate=sample_rate,
                            input=True,
                            input_device_index=input_device_index,
                            frames_per_buffer=frames_per_buffer)

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
