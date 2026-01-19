pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
                echo 'Simulating build step'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
                echo 'Simulating test execution'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
                echo 'Simulating deployment'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
            archiveArtifacts artifacts: '**/*', fingerprint: true
        }
        failure {
            echo 'Pipeline failed — investigate the logs'
        }
    }
}
