pipeline {
    agent any
    environment {
        PYTHON = '/usr/bin/python3'
    }
 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Spoorthi0303/jenkins_try.git'
            }
        }
 
        stage('Build') {
            steps {
                dir('jenkins_try') {
                    sh 'if [ -f requirements.txt ]; then ${PYTHON} -m pip install -r requirements.txt; fi'
                }
            }
        }
 
        stage('Test') {
            steps {
                sh 'python3 manage.py test'
            }
        }
 
        stage('Deploy') {
            steps {
                sh '''
                    pkill gunicorn || true
                    /Users/sdeshpande1/Library/Python/3.9/bin/gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application --daemon
                '''
            }
        }
    }
}
