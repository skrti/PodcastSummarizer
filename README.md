AWS Lambda: Audio Transcription Trigger

This Lambda function is triggered when an audio file (e.g., .mp3) is uploaded to an Amazon S3 bucket. It automatically starts a transcription job using Amazon Transcribe and stores the transcript output in the same S3 bucket.
Features

    Listens to S3 events (e.g., object upload).

    Starts an Amazon Transcribe job for the uploaded audio file.

    Supports English language transcription.

    Stores output transcription results in the same S3 bucket.

Prerequisites

    An S3 bucket with event notifications configured to trigger this Lambda function.

    AWS IAM Role for the Lambda function with the following permissions:

        s3:GetObject

        s3:PutObject

        transcribe:StartTranscriptionJob

How It Works

    A new audio file (e.g., .mp3) is uploaded to the S3 bucket.

    The S3 event triggers the Lambda function.

    Lambda extracts the bucket name and file key.

    It constructs an S3 URI and starts an Amazon Transcribe job.

    The transcription output is saved to the same bucket.


