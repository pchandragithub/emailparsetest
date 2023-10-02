pipeline {
    agent any

    stages {
        stage('Receive and Process Webhook') {
            steps {
                script {
                    def webhookURL = 'http://172.31.24.213:5000/webhook' // Update with your actual URL

                    // Define the payload and content type
                    def payload = """{
                        "emailContent": "example_email_content"
                    }"""
                    def contentType = 'application/json'

                    // Send a POST request to the webhook URL
                    def response = httpRequest(
                        acceptType: contentType,
                        contentType: contentType,
                        httpMode: 'POST',
                        requestBody: payload,
                        url: webhookURL
                    )

                    // Check if the request was successful
                    if (response.status == 200) {
                        echo "Webhook successfully triggered."
                    } else {
                        error "Failed to trigger the webhook. Status code: ${response.status}"
                    }

                    // You can add additional logic to parse the response, if needed
                }
            }
        }
    }
}
