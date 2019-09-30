pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            environment {
                BITBUCKET_COMMON_CREDS = credentials('jenkins-bitbucket-common-creds')
            }
            steps {
                checkout scm
                sh 'cd build && ./build-docker.sh $BITBUCKET_COMMON_CREDS_USR $BITBUCKET_COMMON_CREDS_PSW'
            }
        }
    }
}