# Persian Video Dubbing Pipeline with Full DevOps Integration

This repository demonstrates a complete DevOps-integrated pipeline for Persian video dubbing. The pipeline includes components for ASR (automatic speech recognition), translation, and TTS (text-to-speech) models. It showcases the use of Docker, GitLab CI/CD, Nginx load balancing, database management, monitoring, and security practices. This project is designed to scale and optimize performance while adhering to modern DevOps methodologies.

'''bash
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
