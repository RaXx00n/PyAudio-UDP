# PyAudioUDP

Run PyAudioSend.py on the computer sending the audio and PyAudioRecieve.py on the output computer.

To fix issue with audio playing through speakers on both computers:

On the sending computer, find the subkey representing your audio device under 
> HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Capture

Create a new DWORD (32-bit) Value called "EnableLoopback" and set its value to "1" 
