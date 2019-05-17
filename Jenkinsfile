pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'COMMIT=${GIT_COMMIT} docker-compose -p ${GIT_COMMIT} build'
            }
        }
        stage('Test') {
            steps {
                sh 'COMMIT=${GIT_COMMIT} docker-compose -p ${GIT_COMMIT} up --exit-code-from=tests-worker tests-worker'
                sh 'COMMIT=${GIT_COMMIT} docker-compose -p ${GIT_COMMIT} up --exit-code-from=tests-frontend tests-frontend'
            }
        }
    }
    post {
        always {
           sh 'COMMIT=${GIT_COMMIT} docker-compose -p ${GIT_COMMIT} down -v'
        }
    }
}
