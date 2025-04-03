pipeline {
    agent any
    environment {
        PYTHON = '/usr/bin/python3' // Adjust if necessary
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Spoorthi0303/jenkins_try.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                ${PYTHON} -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Migrations') {
            steps {
                sh '''
                source venv/bin/activate
${PYTHON} manage.py migrate
                '''
            }
        }
        stage('Collect Static Files') {
            steps {
                sh '''
                source venv/bin/activate
${PYTHON} manage.py collectstatic --noinput
                '''
            }
        }
        stage('Run Server') {
            steps {
                sh '''
                source venv/bin/activate
nohup ${PYTHON} manage.py runserver 0.0.0.0:8000 &
                '''
            }
        }
    }
}
