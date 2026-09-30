pipeline {
agent any


environment {
    IMAGE_NAME = 'customer-portal'
    IMAGE_TAG = "build-${BUILD_NUMBER}"
    CONTAINER_NAME = "customer-portal-${BUILD_NUMBER}"
}

stages {

    stage('Checkout') {
        steps {
            echo 'Checking out source code...'
            checkout scm
        }
    }

    stage('Build') {
        steps {
            echo 'Building Customer Portal...'
            bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app\\app.py'
        }
    }

    stage('Test') {
        steps {
            echo 'Running automated tests...'
            bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v'
        }
    }

    stage('Docker Build') {
        steps {
            echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
            bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t %IMAGE_NAME%:%IMAGE_TAG% .'
        }
    }

    stage('Container Verification') {
        steps {
            echo 'Starting temporary container...'
            bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name %CONTAINER_NAME% -p 8090:8080 %IMAGE_NAME%:%IMAGE_TAG%'

            echo 'Waiting for application to start...'
            bat 'powershell.exe -NoProfile -Command "Start-Sleep -Seconds 5"'

            echo 'Checking health endpoint...'
            bat 'curl --fail http://localhost:8090/health'
        }
    }
}

post {
    always {
        echo 'Cleaning up temporary container...'
        bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" stop %CONTAINER_NAME% 2>nul || exit /b 0'
        bat '"C:\\Users\\vasav\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm %CONTAINER_NAME% 2>nul || exit /b 0'
    }
}


}
