import openai
import os

# Step 1: Set up OpenAI API key
openai.api_key = ""

def transcribe_audio(audio_file_path):
    """
    Convert audio to text using OpenAI's Whisper model.
    """
    try:
        print("Reading the audio file...")
        with open(audio_file_path, "rb") as audio_file:
            # Step 2: Call OpenAI API to transcribe
            print("Transcribing audio...")
            response = openai.Audio.transcribe("whisper-1", audio_file)
        print("Transcription completed!")
        return response.get("text", "")
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def main():
    # Step 3: Specify the path to your audio file
    audio_file_path = "example.wav"  # Replace with your file path
    
    if not os.path.exists(audio_file_path):
        print(f"Audio file not found: {audio_file_path}")
        return

    # Step 4: Perform transcription
    transcription = transcribe_audio(audio_file_path)
    
    # Step 5: Output the transcribed text
    if transcription:
        print("\nTranscribed Text:")
        print(transcription)
    else:
        print("No transcription available.")

if __name__ == "__main__":
    main()


