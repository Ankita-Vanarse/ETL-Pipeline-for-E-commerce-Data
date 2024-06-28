# ETL-Pipeline-for-E-commerce-Data

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process and analyze e-commerce transaction data using AWS services such as Lambda, S3, EC2, and CloudWatch. The project involves extracting data from an S3 bucket, transforming it using Pandas, and loading it into a MySQL/PostgreSQL database hosted on an EC2 instance.

## Project Structure

1. etl_project
   │
2. lambda
   └── lambda_function.py
   │
3.  ec2
   └── setup_ec2.sql
   │
4.  reports
   └── generate_report.py
   │
   └──  requirements.txt
   └── README.md
