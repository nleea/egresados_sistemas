pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./scripts/build/build.sh"
            }
        }
        stage('Test') {
            steps {
                sh "./scripts/test/test.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "./scripts/deploy/deploy.sh"
            }
        }
    }
}