pipeline {
    agent any

    environment {
        IMAGE_NAME = 'tviy_login/lab3-app'
        DOCKER_CREDS = 'dockerhub-creds' 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            agent {
                docker { 
                    image 'python:3.9-alpine' 
                    args '-u root' 
                }
            }
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'python -m unittest discover -p "test_*.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_CREDS) {
                        dockerImage.push()
                        dockerImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                sh "docker rmi ${IMAGE_NAME}:latest || true"
                sh "docker rmi ${IMAGE_NAME}:${env.BUILD_NUMBER} || true"
            }
        }
    }
}
