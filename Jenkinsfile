
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Flask Docker image'
                bat 'docker build -t flask-cicd-app .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests inside Docker'
                bat 'docker run --rm flask-cicd-app pytest -v'
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
