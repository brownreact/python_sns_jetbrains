def slackChannel = "#data-science"

properties([
    parameters([
        string(name: 'releaseType', description: "major, minor, or patch", defaultValue: 'minor')
   ])
])

node('slave-medium') {
    wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm', 'defaultFg': 1, 'defaultBg': 2]) {
        wrap([$class: 'TimestamperBuildWrapper']) {
            env.RELEASE_TYPE = releaseType
            try {   
                stage('checkout') {
                    checkout scm
                }
		stage('build') {
            echo 'Building'
                    sh "cd build && ./build-docker.sh browndocker Maths4ever8!"
                }               		   
                if (env.BRANCH_NAME == 'master') {             
                    stage('notify slack') {
                        slackSend channel: slackChannel, color: '#2ECC71', message: "Push ${JOB_NAME} (release type: ${env.RELEASE_TYPE}) to Artifactory - Complete - <${BUILD_URL}|See the build>"
                    }
                }
            }
            catch(error) {
                slackSend channel: slackChannel, color: '#CC3D2E', message: "Push ${JOB_NAME} (release type: ${env.RELEASE_TYPE}) to Artifactory - Failed - <${BUILD_URL}|See the build>"
                currentBuild.result = "FAILURE"
                throw error
            }
            stage('clean workspace') {
                cleanWs()
            }
        }
    }
}