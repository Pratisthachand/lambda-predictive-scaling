# Predictive Scaling for AWS Lambda Using Machine Learning to Reduce Cold Starts

This project contains the source code and supporting files for a serverless application designed for my senior seminar. The application investigates the effectiveness of predictive machine learning models in proactively managing AWS Lambda concurrency to reduce cold starts. The project utilizes the AWS Serverless Application Model (SAM) CLI to build, test, and deploy the application.

## Project Structure

- add_one - Contains the source code for the Lambda function. This function has been specifically designed to simulate cold start latency for accurate measurement.
- events - Includes test event payloads for invoking the Lambda function locally.
- tests - Holds unit and integration tests for the application.
- template.yaml - The Infrastructure as Code blueprint for the entire serverless application, defining all AWS resources.

## Load Testing

I will use the Locust load testing tool to simulate various traffic patterns and collect performance metrics. The locustfile.py in this repository contains three distinct user classes to simulate periodic, bursty, and mixed workloads.

## Monitoring & Metrics

All performance metrics are automatically collected in Amazon CloudWatch. After running a load test, I will analyze the following key metrics to establish the performance baseline: duration, invocations, throttles.
