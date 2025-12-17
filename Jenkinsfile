pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code available'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Simulated build step'
            }
        }

        stage('Test') {
            steps {
                echo 'Simulated test step'
            }
        }
    }
}
