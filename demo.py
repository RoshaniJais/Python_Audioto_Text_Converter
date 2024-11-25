import boto3
import openai
import os

# Step 1: Configure AWS and OpenAI credentials
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
S3_BUCKET_NAME = ""
S3_FILE_KEY = ""  # File key in the S3 bucket

openai.api_key = ""

def download_audio_from_s3(bucket_name, file_key, download_path):
    """
    Download a WAV file from an S3 bucket.
    """
    try:
        print("Connecting to S3...")
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        print(f"Downloading file from bucket '{bucket_name}'...")
        s3.upload_file(bucket_name, file_key, download_path)
        print("Download completed.")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")
        raise

def transcribe_audio_with_whisper(file_path):
    """
    Transcribe audio using OpenAI Whisper.
    """
    try:
        print("Transcribing audio with Whisper...")
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        print("Transcription completed.")
        return response.get("text", "")
    except Exception as e:
        print(f"Error during transcription: {e}")
        raise

def main():
    # Step 2: Local path to save the downloaded file
    local_audio_path = "temp_audio.wav"

    try:
        # Step 3: Download the audio file from S3
        download_audio_from_s3(S3_BUCKET_NAME, S3_FILE_KEY, local_audio_path)

        # Step 4: Transcribe the downloaded audio file
        transcription = transcribe_audio_with_whisper(local_audio_path)

        # Step 5: Output the transcribed text
        print("\nTranscribed Text:\n")
        print(transcription)

    finally:
        # Step 6: Clean up the temporary file
        if os.path.exists(local_audio_path):
            os.remove(local_audio_path)
            print("Temporary file deleted.")

if __name__ == "__main__":
    main()
