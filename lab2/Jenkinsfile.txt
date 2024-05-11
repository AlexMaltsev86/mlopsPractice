pipeline {
    agent any
    stages {

        stage('data generation') {
            steps {
                bat  '''
                    C://Users//malet//AppData//Local//Programs//Python//Python311//python C://ProgramData//Jenkins//.jenkins//workspace//lab2//lab2//data_creation.py
                    '''
            }
        }        
        stage('Preparation environment') {
            steps {
                bat  '''
                    python3 C://Users//malet//AppData//Local//Programs//Python//Python311//python C://ProgramData//Jenkins//.jenkins//workspace//lab2//lab2//model_preprocessing.py
                    '''
            }
        }
        stage('Model training') {
            steps {
                bat  '''
                    python3 C://Users//malet//AppData//Local//Programs//Python//Python311//python C://ProgramData//Jenkins//.jenkins//workspace//lab2//lab2//model_preparation.py
                    '''
            }
        }
        stage('Model testing') {
            steps {
                bat  '''
                    python3 C://Users//malet//AppData//Local//Programs//Python//Python311//python C://ProgramData//Jenkins//.jenkins//workspace//lab2//lab2//model_testing.py
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
