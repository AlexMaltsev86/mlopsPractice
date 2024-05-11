pipeline {
    agent any
    stages {

        stage('data generation') {
            steps {
                sh '''
                    python3 lab2/data_creation.py
                    '''
            }
        }        
        stage('Preparation environment') {
            steps {
                sh '''
                    python3 lab2/model_preprocessing.py
                    '''
            }
        }
        stage('Model training') {
            steps {
                sh '''
                    python3 lab2/model_preparation.py
                    '''
            }
        }
        stage('Model testing') {
            steps {
                sh '''
                    python3 lab2/model_testing.py
                    '''
            }
        }
    }
    post {
        always {
            echo 'The pipeline is finished!'
        }
        success {
            echo 'The build was successful!'
        }
        failure {
            echo 'The build failed.'
        }
    }
}
