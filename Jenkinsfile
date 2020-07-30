pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'docker pull parazit13/WorldOfGames:latest'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t wog_mainScores_test .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run --rm -d -port 8777:5000 wog_mainScores_test'
            }
        }
        stage('Test') {
            steps {
		        sh 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop wog_mainScores_test'
		        sh 'docker tag wog_mainScores_test parazit13/WorldOfGames'
		        sh 'docker push parazit13/WorldOfGames'
            }
        }
    }
}
