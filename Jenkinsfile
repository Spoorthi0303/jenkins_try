pipeline {
    agent any  // Runs on any available agent
 
    stages {
        stage('Clone Repository') {
            steps {
            git branch: 'main', url: 'https://github.com/Spoorthi0303/jenkins_try.git'
            }
        }
 
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
 
        stage('Run Tests') {
            steps {
            sh 'python manage.py test'
            }
        }
 
        stage('Deploy') {
            steps {
                sh '''
                python manage.py migrate
                python manage.py collectstatic --noinput
                sudo systemctl restart apache2
                '''
            }
        }
    }
}