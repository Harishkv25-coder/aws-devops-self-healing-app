# Automated CI/CD Pipeline with Self-Healing Web Application on AWS

## Project Overview

This project demonstrates an automated DevOps workflow for deploying and monitoring a Python Flask web application on AWS.

It integrates GitHub Actions for CI/CD, AWS Systems Manager for remote deployment and recovery, Amazon CloudWatch for monitoring and logging, and AWS Lambda with EventBridge Scheduler for automated application health checks and self-healing.

The objective is to reduce manual intervention, improve application availability, and demonstrate practical AWS and DevOps skills.

## Architecture

**Workflow:**

1. Developer pushes code to GitHub.
2. GitHub Actions automatically runs Python tests.
3. If tests pass, the deployment workflow connects to AWS using OIDC authentication.
4. AWS Systems Manager sends deployment commands to the EC2 instance.
5. The Flask application runs as a systemd service using Gunicorn.
6. CloudWatch collects system and application logs.
7. EventBridge Scheduler invokes the recovery Lambda function every five minutes.
8. Lambda checks application health through AWS Systems Manager.
9. If the application is unhealthy, Lambda attempts to restart the application service and verifies recovery.
10. Scheduled backup scripts upload application backups to Amazon S3.

## AWS Services and Tools

| Service / Tool | Purpose |
|---|---|
| Amazon EC2 | Hosts the Flask application |
| AWS IAM | Access control and permissions |
| GitHub Actions | CI/CD automation |
| GitHub OIDC | Secure GitHub-to-AWS authentication |
| AWS Systems Manager | Remote deployment and recovery commands |
| AWS Lambda | Automated health checks and recovery |
| Amazon EventBridge Scheduler | Triggers periodic health checks |
| Amazon CloudWatch | Monitoring and log collection |
| Amazon S3 | Application backup storage |
| Python / Flask | Web application |
| Gunicorn | Python application server |
| systemd | Application service management |
| Git | Version control |

## Application Details

**Application:** AWS DevOps Self-Healing Web Application

**Framework:** Flask

**Version:** 1.1.0

**Endpoints:**

- `/` – Application home page
- `/health` – Application health check
- `/version` – Displays application version

## CI/CD Pipeline

The GitHub Actions workflow automates:

- Python environment setup
- Dependency installation
- Automated unit testing
- Deployment to AWS EC2
- Remote execution through AWS Systems Manager

The deployment workflow uses GitHub OIDC authentication rather than storing long-lived AWS access keys in GitHub repository secrets.

## Self-Healing Mechanism

An EventBridge Scheduler triggers the Lambda recovery function every five minutes.

The Lambda function:

1. Sends a health-check command to the EC2 instance using Systems Manager.
2. Checks the application's health endpoint.
3. Records the command result in CloudWatch Logs.
4. Attempts to restart `devops-webapp.service` if the application is unhealthy.
5. Checks the application again and records the recovery result.

## Monitoring and Logging

Amazon CloudWatch Agent collects:

- System logs from `/var/log/messages`
- Cloud-init logs from `/var/log/cloud-init-output.log`
- Application service logs from journald

Configured CloudWatch log groups:

- `DevOps-EC2-System-Logs`
- `DevOps-EC2-CloudInit-Logs`
- `DevOps-EC2-Application-Logs`

Log retention is configured for seven days.

## Backup and Restore

Application backups are created as timestamped archives and uploaded to Amazon S3.

The project includes:

- Automated backup uploads
- S3 access restricted through IAM permissions
- S3 Block Public Access enabled
- Server-side encryption using SSE-S3
- Backup download and extraction validation

## Security Practices

- GitHub OIDC authentication for CI/CD
- IAM policies scoped to required resources where practical
- EC2 access through AWS Systems Manager Session Manager
- SSH access restricted to the administrator's public IP
- S3 public access blocked
- S3 server-side encryption enabled
- No AWS access keys committed to the repository
- Separate IAM roles for EC2, Lambda and EventBridge Scheduler

## Repository Structure

```text
aws-devops-self-healing-app/
│
├── .github/
│   └── workflows/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── scripts/
│
├── docs/
│   └── screenshots/
│
├── .gitignore
└── README.md
```

## Testing and Validation

The project has been validated through:

- Successful local Python unit tests
- Successful GitHub Actions CI execution
- AWS EC2 application deployment
- Application health endpoint verification
- CloudWatch log collection
- Scheduled Lambda health checks
- Successful manual self-healing recovery test
- S3 backup upload and restore validation

## Skills Demonstrated

- AWS EC2 and IAM
- Git and GitHub
- GitHub Actions CI/CD
- Python and Flask
- AWS Systems Manager
- AWS Lambda
- Amazon EventBridge
- Amazon CloudWatch
- Amazon S3
- Linux administration
- systemd service management
- Monitoring, troubleshooting and recovery automation

## Project Objective

This project demonstrates how DevOps practices and AWS services can be integrated to automate application delivery, monitoring, backup and recovery.

**Author:** Harish K V

**GitHub Repository:** https://github.com/Harishkv25-coder/aws-devops-self-healing-app
