import os
import sys
from whisper_live.client import TranscriptionClient

def run_client_microphone(lang="fr", model="base"):
    # Placeholder for the actual implementation of running the client with a microphone
    print(f"Running WhisperLive client with microphone input")
    print(f"Model size: {model}")
    print(f"Language: {lang}")
    
    # Example of setting up the transcription client for microphone input
    client = TranscriptionClient(
        "localhost",
        9090,
        lang=lang,
        translate=False,
        model=model,
        use_vad=True,  
    )

    # Start the client 
    client()

if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run WhisperLive client from microphone.")
    parser.add_argument("--lang", type=str, default="fr", help="Language for transcription (default: 'fr').")
    parser.add_argument("--model", type=str, default="base", help="Model size for transcription (default: 'small').")

    args = parser.parse_args()

    # Run the client with microphone input
    run_client_microphone(args.lang, args.model)
