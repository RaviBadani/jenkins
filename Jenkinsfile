
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub'
                checkout scm
            }
        }

        stage('System Information') {
            steps {
                echo 'Checking Jenkins environment'

                sh '''
                    echo "===== SYSTEM INFORMATION ====="
                    whoami
                    pwd
                    uname -a

                    echo "===== DOCKER VERSION ====="
                    docker --version

                    echo "===== DOCKER IMAGES ====="
                    docker images

                    echo "===== RUNNING CONTAINERS ====="
                    docker ps
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Flask Docker image'

                sh 'docker build -t flask-cicd-app .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests inside Docker'

                sh 'docker run --rm flask-cicd-app pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting Flask application'

                sh '''
                    docker rm -f flask-jenkins-app 2>/dev/null || true

                    docker run -d \
                    --name flask-jenkins-app \
                    -p 5001:5000 \
                    flask-cicd-app

                    sleep 3

                    docker ps
                '''
            }
        }

        stage('Verify Application') {
            steps {
                echo 'Checking application health'

                sh '''
                    docker run --rm --network host \
                    curlimages/curl:latest \
                    -f http://127.0.0.1:5001/health
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}
