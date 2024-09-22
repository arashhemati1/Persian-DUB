# Persian Video Dubbing Pipeline with Full DevOps Integration

This repository demonstrates a complete DevOps-integrated pipeline for Persian video dubbing. The pipeline includes components for ASR (automatic speech recognition), translation, and TTS (text-to-speech) models. It showcases the use of Docker, GitLab CI/CD, Nginx load balancing, database management, monitoring, and security practices. This project is designed to scale and optimize performance while adhering to modern DevOps methodologies.

 ```bash
persian-dubbing-devops/
├── asr/
│   ├── Dockerfile
│   ├── asr_service.py
│   └── requirements.txt
├── translation/
│   ├── Dockerfile
│   ├── translation_service.py
│   └── requirements.txt
├── tts/
│   ├── Dockerfile
│   ├── tts_service.py
│   └── requirements.txt
├── database/
│   ├── postgres/
│   │   └── Dockerfile
│   ├── mongo/
│   │   └── Dockerfile
├── monitoring/
│   ├── prometheus/
│   ├── grafana/
│   ├── elk/
│   └── docker-compose.yml
├── nginx/
│   └── nginx.conf
├── scripts/
│   ├── backup.sh
│   ├── docker_clean.sh
│   └── deployment.sh
├── tests/
│   ├── load_test/
│   │   └── locustfile.py
│   └── unit_tests/
│       └── test_services.py
├── .gitlab-ci.yml
├── README.md
└── docker-compose.yml

# Persian Video Dubbing Pipeline with Full DevOps Integration

## Overview
This repository demonstrates a complete Persian dubbing pipeline integrated with modern DevOps practices. The project includes ASR (speech recognition), translation, and TTS (text-to-speech) services, all containerized using Docker and managed via GitLab CI/CD pipelines. Additionally, it includes Nginx for load balancing, Prometheus and Grafana for monitoring, and ELK for logging.

## Features
- **Linux Server Management**: Deployed on Linux with automation scripts for backup and maintenance.
- **Nginx Load Balancing**: Configured to scale services across multiple containers.
- **Containerization**: Each service (ASR, Translation, TTS) is containerized using Docker.
- **Database Management**: PostgreSQL and MongoDB databases are used to store metadata and logs.
- **Monitoring & Logging**: Prometheus, Grafana, and the ELK stack monitor service health and centralize logs.
- **CI/CD Pipeline**: Automated testing, building, and deployment using GitLab CI/CD.

## Setup Instructions
1. Clone the repository.
2. Set up the environment by running `docker-compose up -d`.
3. Access the ASR, Translation, and TTS services via Nginx.
4. View monitoring dashboards at `localhost:3000` (Grafana) and `localhost:5601` (Kibana).

## Contributions
Feel free to submit issues or pull requests!
