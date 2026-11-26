# Automated CI/CD Pipeline with Self-Healing Web Application on AWS

## Project Overview

This project demonstrates an automated CI/CD pipeline and a self-healing web application hosted on AWS.

The application is built using Python Flask and deployed on an Amazon EC2 instance through GitHub Actions. AWS Systems Manager (SSM) enables secure remote deployment without requiring SSH access from the pipeline.

The solution also includes automated application health checks, recovery using AWS Lambda and EventBridge Scheduler, centralized monitoring with Amazon CloudWatch, email notifications through Amazon SNS, and application backups to Amazon S3.

### Project Objectives

- Automate application testing and deployment.
- Implement secure AWS access using GitHub OIDC.
- Monitor EC2 metrics and application logs.
- Automatically recover the application when its health check fails.
- Back up application files to Amazon S3.
- Demonstrate practical AWS DevOps skills.

## AWS Architecture

The following diagram illustrates the architecture of the Automated CI/CD Pipeline with Self-Healing Web Application on AWS.

![AWS Project Architecture](docs/aws-architecture.png)

### Architecture Workflow

1. **Source Code:** Application code is maintained in GitHub.
2. **CI/CD:** GitHub Actions runs automated tests and deploys the application to EC2.
3. **Secure Authentication:** AWS IAM OIDC provides secure GitHub Actions access to AWS.
4. **Application Hosting:** Amazon EC2 hosts the Flask web application using Gunicorn.
5. **Monitoring:** Amazon CloudWatch collects system metrics and application logs.
6. **Notifications:** Amazon SNS sends email notifications.
7. **Automated Health Checks:** Amazon EventBridge Scheduler invokes Lambda every five minutes.
8. **Self-Healing:** AWS Lambda checks application health and uses AWS Systems Manager to restart the application when unhealthy.
9. **Backup:** A scheduled backup script creates application archives and uploads them to Amazon S3.