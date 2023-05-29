pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout source code from version control system (e.g., Git)
                git 'https://github.com/NuelUzoma/Portfolio-Project.git'

                // Build Docker image
                script {
                    docker.build('ubuntu:latest', '--file Dockerfile .')
                }
            }
        }

        stage('Test') {
            steps {
                // Run tests inside a Docker container
                script {
                    docker.image('ubuntu:latest').inside {
                        sh 'mvn test' // Example: Run tests with Maven
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy Docker image
                script {
                    withDockerRegistry('http://107.23.96.11:5000') {
                        docker.image('ubuntu:latest').push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Build, test, and deploy successful'
            // Additional actions to perform on success
        }
        failure {
            echo 'Build, test, or deploy failed'
            // Additional actions to perform on failure
        }
    }
}
