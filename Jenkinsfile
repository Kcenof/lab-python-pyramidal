pipeline {
    agent any

    environment {
        // ЗАМІНИ НА СВІЙ ЛОГІН
        IMAGE_NAME = 'skabserhii/Ecslab' 
        DOCKER_CREDS = 'dockerhub-creds'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests inside Docker container...'
                    bat 'docker run --rm -v "%CD%":/app -w /app python:3.9-alpine sh -c "pip install -r requirements.txt && python -m unittest discover -p test_*.py"'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building image...'
                    bat "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        bat "docker login -u %USER% -p %PASS%"
                        bat "docker push ${IMAGE_NAME}:latest"
                        bat "docker logout"
                    }
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    bat "docker rmi ${IMAGE_NAME}:latest || exit 0"
                }
            }
        }
    }
}
