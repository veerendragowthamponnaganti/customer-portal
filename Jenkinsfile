pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Customer Portal...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
            }
        }

        stage('Container Verification') {
            steps {
                echo 'Verifying Docker container...'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up temporary container...'
            }
        }
    }
}