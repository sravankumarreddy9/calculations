pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = 'github credentials ID' // Set this in Jenkins credentials
        GIT_REPO_URL = 'https://github.com/sravankumarreddy9/calculations.git' // Update with your repo URL
        BRANCH_NAME = 'master' // Change if your branch is 'main'
        PYTHON_SCRIPT_PATH = './calcuateDevices.py' // Path to your Python script
        EMAIL_RECIPIENT = 'venkatasravankumarreddy10@gmail.com' 
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Cloning the repository
                    checkout([$class: 'GitSCM', 
                        branches: [[name: "*/${BRANCH_NAME}"]],
                        userRemoteConfigs: [[
                            url: "${GIT_REPO_URL}",
                            credentialsId: "${GIT_CREDENTIALS_ID}"
                        ]]
                    ])
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Python script and capture the output
                    def scriptOutput = sh(script: "python3 ${PYTHON_SCRIPT_PATH}", returnStdout: true).trim()
                    echo "Python script output:\n${scriptOutput}"

                    // Save output to an environment variable for use in the email
                    env.PYTHON_OUTPUT = scriptOutput
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
            // Send email with Python script output as notification
            emailext(
                to: "${EMAIL_RECIPIENT}",
                subject: "Jenkins Pipeline Success: Python Script Results",
                body: "The Python script executed successfully. Here is the output:\n\n${env.PYTHON_OUTPUT}"
            )
        }
        failure {
            echo "Pipeline failed. Check the logs!"
            // Send email notification on failure
            emailext(
                to: "${EMAIL_RECIPIENT}",
                subject: "Jenkins Pipeline Failure: Python Script Execution",
                body: "The Python script failed. Please check the Jenkins logs for details."
            )
        }
    }
}