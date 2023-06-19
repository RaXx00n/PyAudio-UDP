#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⣴⣶⣤⠀⣿⣿⣿
#⡿⢛⣉⣉⣉⣉⡛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣡⣴⠏⠁⠀⡚⠀⢸⣿⣿
#⠁⣿⠉⢀⡉⠉⢿⣷⣄⠈⠉⠁⣠⣀⣤⡀⣤⣤⣀⣴⠂⢺⠧⠀⠀⠀⠀⠀⣾⣿⣿
#⠀⢷⣀⠀⠀⠀⠈⠙⣷⠀⠀⣿⣿⣿⣿⣿⢿⣿⡟⠃⠠⢄⣀⢀⡴⠀⣠⣾⣿⣿⣿
#⣧⠈⠣⣦⠀⠀⠀⠀⠉⠸⠛⠃⠉⠋⠹⠀⠃⠁⠀⠀⠀⠺⣟⣷⣦⣄⠙⠿⣿⣿⣿
#⣿⣇⢈⢿⣷⣾⣦⡤⢴⣿⣶⡀⢠⣔⣤⣤⡀⠀⠲⣾⣿⣶⣿⣿⣿⣿⣷⣄⠈⢻
#⣿⠏⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⡻⣿⠀⠘⠿⡟⠡⠄⢉⡼⢿⣿⣿⣦⠈
#⡏⣨⣿1⣿3⣿8⣿⣿⠟⡁⠐⠃⠈⠀⠐⠀⠀⣀⢠⡤⣾⠃⠀⠉⠛⠛⢠
#⠁⣿⣿⣿⣿⣿⣿⣿⠏⠁⠘⠿⣶⣤⠴⠶⢟⣰⣶⣾⣿⣷⣤⣀⠀⠀⠀⠀⣠⣾
#⡀⢿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠉⠁⢠⣴⣿⣿⣿⣿⢿⣟⠿⣿⡆⠀⢀⣾⣿⣿
#⣷⡄⠛⠟⠃⠀⠀⠀⠀⠀⠀⢠⣤⣶⣿⣿⣿⣿⣿⡃⠈⠁⠀⠘⣡⣾⣿⣿⣿⣿
#⣿⣿⣶⣤⣤⣤⣄⣀⣀⣀⣀⣀⣈⣛⣉⣉⡙⠋⠋⠁⠀⢀⣠⣾⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⣿⣿⣿⣿                         ⣿⣿⣿⣿⣿
#⣿⣿⣿⣿  Github.com/RaXx00n/    ⣿⣿⣿⣿⣿
#⣿⣿⣿⣿                         ⣿⣿⣿⣿⣿
#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

import pyaudio
import socket

## Where it's gonna listen
listen_ip = '0.0.0.0'
listen_port = 1138

#x# Audio parameters
sample_rate = 48000
frames_per_buffer = 4096
buffer_size = frames_per_buffer * 8 

#x# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((listen_ip, listen_port))

#x# Initialize PyAudio
audio = pyaudio.PyAudio()

#x# Open the audio stream for playback
playback_stream = audio.open(format=pyaudio.paInt16,
                             channels=2,
                             rate=sample_rate,
                             output=True,
                             frames_per_buffer=frames_per_buffer)

#x# Start receiving and playing audio
while True:
    # Receive audio data from the network
    audio_data, _ = server_socket.recvfrom(buffer_size)

    # Play the received audio
    playback_stream.write(audio_data)

# Close the stream and terminate PyAudio
playback_stream.stop_stream()
playback_stream.close()
audio.terminate()
server_socket.close()
