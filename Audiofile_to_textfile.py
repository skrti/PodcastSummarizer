import json
import boto3
import urllib.parse
import re

s3 = boto3.client("s3")
transcribe = boto3.client("transcribe")

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))  # Debugging

    # Ensure the event contains 'Records'
    if "Records" not in event:
        return {
            "statusCode": 400,
            "body": json.dumps("Invalid event structure: No 'Records' key found")
        }

    record = event["Records"][0]  # First record
    bucket_name = record["s3"]["bucket"]["name"]
    file_key = record["s3"]["object"]["key"]


    file_key = urllib.parse.unquote_plus(file_key)


    file_uri = f"s3://{bucket_name}/{file_key}"
    # Define Transcription Job Name
    job_name = re.sub(r"[^0-9a-zA-Z._-]", "-", file_key)

    try:
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={"MediaFileUri": file_uri},
            MediaFormat="mp3",  
            LanguageCode="en-US",
            OutputBucketName=bucket_name
        )

        print(f"Transcription started for {file_key}")
        return {
            "statusCode": 200,
            "body": json.dumps("Transcription started successfully")
        }

    except Exception as e:
        print(f"Error processing {file_key}: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
    

