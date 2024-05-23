# WhisperLive

<h2 align="center">
  <a href="https://www.youtube.com/watch?v=0PHWCApIcCI"><img
src="https://img.youtube.com/vi/0PHWCApIcCI/0.jpg" style="background-color:rgba(0,0,0,0);" height=300 alt="WhisperLive"></a>
  <br><br>Live Whisper.
<br><br>
</h2>



## Installation

### Docker:
- Ensure Docker is installed and running on your machine.

### Run Setup Script:
Ensure you have the required libraries installed by running the setup.bat script:

```bash
setup.bat
```

## Running the Server
To run the WhisperLive server with GPU support, use the following command:

```bash
docker run -it --gpus all -p 9090:9090 ghcr.io/collabora/whisperlive-gpu:latest
```

## Running the Client
To transcribe a YouTube video

### Run the Client Script (from youtube link):
To transcribe a YouTube video with default settings, run:

```bash
python run_client_YT.py
```
Default settings:

1. YouTube URL: https://www.youtube.com/watch?v=cx4LaLSdCa4&ab_channel=BloombergTelevision
2. Language: en (English)
3. Model: small

To run the script with custom values:
```bash
python run_client_YT.py --url "YOUR_YOUTUBE_URL" --lang "LANGUAGE_CODE" --model "MODEL_SIZE"
```

### Running the Client from Microphone
To run the WhisperLive client with microphone input, use the run_client.py script:

```bash
python run_client.py
```

Default settings:

1. Language: fr (French)
2. Model: base

To run the script with custom values:

```bash
python run_client.py --lang "LANGUAGE_CODE" --model "MODEL_SIZE"
```

