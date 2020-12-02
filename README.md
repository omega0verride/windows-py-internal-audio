# windows-py-internal-audio
This script finds the device that is capable of using loopback, then opens a stream to get audio directly from the system. 

It can be integrated with audio visualisation/analysis projects.  
The script automatically detects the device and opens a loopback stream.  
You can get an audio stream directlly from your computer internal audio without having to specify stream parameters or detect the audio device that is capable of loopback.  

A loopback stream is the best choice because you don't have to deal with microphone noise, aux input or virtual audio devices.

# Usage

import the script (make sure you have it in the same directory and you have an empty "__init__.py" file)
```
import audio_loopback_device as lbdevice
import numpy as np
```

Opening a stream that gets data from internal audio is as simple as:
```
    stream = lbdevice.get_loopback_stream()  # opens a PyAudio stream using the loopback device
```

If you just want to find the device that supports loopback:
```
device = lbdevice.get_loopback_device()  # gets current output device that supports audio loopback
device_index = lbdevice.get_loopback_device_id()  # returns device id if you want to use it with PyAudio
```


**Make sure you install PyAudio from this repo:** https://github.com/intxcc/pyaudio_portaudio/releases/  
It is the only version that offers loopback stream.  
Make sure the precompiled wheel matches your python version.  
