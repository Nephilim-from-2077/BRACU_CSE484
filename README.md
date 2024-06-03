"# BRACU_CSE484" 
Introduction to AWS Rekognition:

AWS Rekognition is a service that provides computer vision capabilities for analyzing images and videos.
It offers pre-built machine learning models for various tasks, including face recognition.
Steps to Create the Face Recognition Service:

Step 1: Create an S3 Bucket and Upload Images
Create an S3 bucket to store images.
Upload images of famous persons to the S3 bucket, associating metadata with each image (e.g., person's name).
Step 2: Create an AWS Lambda Function
AWS Lambda will serve as the backend for the application.
Set up a Lambda function to trigger whenever a new image is uploaded to the S3 bucket.
This function will populate the index of Amazon Rekognition with face prints.
Step 3: Populate Amazon Rekognition Index
The Lambda function analyzes the uploaded images, generates face prints, and stores them along with corresponding names in a DynamoDB table.
Step 4: Test the Face Recognition Service
Use the Amazon Rekognition API to search for faces in an image and recognize the persons.
Test the service with images to verify if it correctly recognizes the persons.
Implementation:

Create an S3 bucket, DynamoDB table, and Lambda function.
Use Python to write code for uploading images to S3, triggering the Lambda function, and testing the recognition service.
