import boto3
import openai


# Step 1: Configure AWS and OpenAI credentials
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
S3_BUCKET_NAME = ""
S3_FILE_KEY = ""  # File key in the S3 bucket

#Step 2: Adding openAI api key to access whishper model
openai.api_key = ""

#Step 3: Defining funcation to check the aws and s3 bucket connecation

def Verifying_Connecation():
    """
    verifying aws connecation with s3 bucket connecting or not
    """
    try:
        print("Connecting to S3...")
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        
    except Exception as e:
        print(f"Error while connecting to S3: {e}")
        raise

#Step 4: Defining funcation to convert audion wav file to text using whishper machine learning model 

def transcribe_audio_with_whisper(S3_FILE_KEY):
    """
    Transcribe audio using OpenAI Whisper.
    """
    try:
        print("Transcribing audio with Whisper...")

        with open(S3_FILE_KEY, "rb") as audio_file: 
            response = openai.Audio.transcribe("whisper-1", audio_file) #whishper is a machine leraning model for speech recognition and transcription
        '''
            openai.Audio.transcribe Reads the WAV file.
            Sends it to the OpenAI Whisper API for transcription.
            Returns the transcription as text.
        '''
        print("Transcription completed.")
        return response.get("text", "")
    except Exception as e:
        print(f"Error during transcription: {e}")
        raise

def main():

    try:
        # Step 5: checking s3 bucket  Connecation
        Verifying_Connecation()

        # Step 6: Transcribe the downloaded audio file
        transcription = transcribe_audio_with_whisper(S3_FILE_KEY)

        # Step 7: Output the transcribed text
        print("\nTranscribed Text:\n")
        print(transcription)

    except Exception as e:
        print(f"Error during transcription: {e}")
        raise

if __name__ == "__main__":
    main()

