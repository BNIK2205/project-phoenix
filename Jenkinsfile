pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Running unit tests'
                bat 'echo Simulating test execution'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
