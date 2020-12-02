# windows-py-internal-audio
This script finds the device that is capable of using loopback, then opens a stream to get audio directly from system. 

It can be integrated with audio visualisation/analysis projects.  
The script automatically detects the device and opens a loopback stream.  
You can get an audio stream directlly from your computer internal audio without having to specify stream parameters or detect audio device that is capable of loopback.  

A loopback stream is the best choice because you don't have to deal with microphone noise, aux input or virtual audio devices.

**Make sure you install PyAudio from this repo:** https://github.com/intxcc/pyaudio_portaudio/releases/  
It is the only version that offers loopback stream.  
Make sure the precompiled wheel matches your python version.  
