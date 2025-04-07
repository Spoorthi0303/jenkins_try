pipeline {
    agent any
 
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Spoorthi0303/jenkins_try.git'
            }
        }
 
        stage('Install Requirements') {
            steps {
                dir('jenkins_try') {
                    sh 'if [ -f requirements.txt ]; then /usr/bin/python3 -m pip install -r requirements.txt; fi'
                }
            }
        }
 
        stage('Collect Static Files') {
            steps {
                dir('jenkins_try/myproject') {
                sh '/usr/bin/python3 manage.py collectstatic --noinput'
                }
            }
        }
 
        stage('Run Gunicorn') {
            steps {
                dir('jenkins_try') {
                    sh 'pkill gunicorn || true'
                    sh '~/Library/Python/3.9/bin/gunicorn --bind 127.0.0.1:8000 myproject.wsgi:application --daemon'
                }
            }
        }
 
        stage('Reload Nginx') {
            steps {
                sh 'sudo /opt/homebrew/bin/nginx -s reload'
            }
        }
    }
 
    post {
        success {
            echo 'Deployment complete and Django server started.'
        }
    }
}
