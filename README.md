# Automated CI/CD Pipeline with Self-Healing Web Application on AWS

## Project Overview

This project demonstrates an automated CI/CD pipeline and a self-healing web application hosted on AWS.

The application is built using Python Flask and deployed on an Amazon EC2 instance through GitHub Actions. AWS Systems Manager (SSM) enables secure remote deployment without requiring SSH access from the pipeline.

The solution also includes automated application health checks, recovery using AWS Lambda and EventBridge Scheduler, centralized monitoring with Amazon CloudWatch, email notifications through Amazon SNS, and application backups to Amazon S3.

## Project Objectives

- Automate application testing and deployment.
- Implement secure AWS access using GitHub OIDC.
- Monitor EC2 metrics and application logs.
- Automatically recover the application when its health check fails.
- Back up application files to Amazon S3.
- Demonstrate practical AWS DevOps skills.

## Technologies Used

| Category | Technologies |
|---|---|
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| CI/CD | GitHub Actions |
| Version Control | Git, GitHub |
| Programming Language | Python 3 |
| Web Framework | Flask |
| Application Server | Gunicorn |
| Authentication | AWS IAM OIDC |
| Remote Management | AWS Systems Manager (SSM) |
| Monitoring | Amazon CloudWatch |
| Notifications | Amazon SNS |
| Serverless Recovery | AWS Lambda |
| Scheduling | Amazon EventBridge Scheduler |
| Backup Storage | Amazon S3 |
| Operating System | Amazon Linux 2023 |
| Testing | Python unittest |

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

## Key Project Features

### 1. Automated CI/CD Pipeline

- GitHub Actions automatically triggers the pipeline when code is pushed to the main branch.
- Runs Python unit tests before deployment.
- Uses AWS IAM OIDC for secure authentication.
- Deploys the application to EC2 through AWS Systems Manager.

### 2. Self-Healing Application

- EventBridge Scheduler invokes the recovery Lambda function every five minutes.
- Lambda checks the application's health endpoint.
- If the application is unhealthy, Lambda uses SSM to restart the application service.
- Performs another health check to verify recovery.

### 3. Monitoring and Logging

- CloudWatch monitors EC2 system metrics.
- CloudWatch Agent collects system and application logs.
- CloudWatch alarms monitor CPU utilization.
- SNS provides email notifications.

### 4. Automated Backup

- A scheduled backup script creates compressed application archives.
- Backup files are uploaded to a private Amazon S3 bucket.
- Backup download and extraction have been manually verified.
- Cron schedules automated backups daily at 2:00 AM IST.

## Testing and Validation Results

The project components were tested and validated to confirm that the CI/CD pipeline, application deployment, monitoring, automated recovery, and backup processes work as expected.

### 1. CI/CD Pipeline Validation

- Python unit tests executed successfully using GitHub Actions.
- Automated deployment to AWS EC2 completed successfully.
- Latest verified GitHub Actions workflow completed with a successful status.
- Both the testing and deployment jobs passed.

### 2. Application Validation

- Flask application service verified as active using systemd.
- Health endpoint (`/health`) returned `{"status":"healthy"}`.
- Version endpoint (`/version`) returned version `1.1.0`.
- Application health was independently verified after deployment.

### 3. Monitoring and Logging

- CloudWatch EC2 monitoring configured.
- CPU monitoring and CloudWatch alarms configured.
- System, CloudInit, and application logs successfully collected in CloudWatch Logs.
- SNS email subscription confirmed.
- Direct SNS test notification successfully received.

### 4. Self-Healing Validation

- Lambda recovery function successfully tested by stopping the application service.
- EventBridge Scheduler automatically invoked the recovery function.
- Application service was restarted successfully.
- Application health was independently verified after recovery.
- Scheduled health checks successfully detected and recovered an unhealthy application.

### 5. Automated Backup Validation

- Application backup script successfully created compressed archives.
- Manual S3 backup upload verified.
- Backup download and extraction manually tested.
- Cron-based scheduled backups successfully executed on two consecutive days.
- Both scheduled backup files confirmed in the private Amazon S3 bucket.
- Scheduled backups configured to execute daily at 2:00 AM IST.

### Validation Summary

The project successfully demonstrates automated CI/CD deployment, application health monitoring, scheduled self-healing, centralized logging, and automated application backups using AWS services.

The implementation provides practical experience with AWS cloud infrastructure, automation, monitoring, deployment, and recovery operations.