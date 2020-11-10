#!/usr/bin/env groovy

pipeline {
    agent { label 'linux' }
    parameters {
        string(name: 'org_jobs_list_to_copy', defaultValue: '', description: 'Comma-seperated values of jobs to be copied. e.g Job_name1,Job_name2,Job_name3')
        string(name: 'source_instance_url', defaultValue: '', description: 'Source Instance URL where JOBS need to be copied FROM e.g https://svxx-jenstg-xxx.core.cvent.org/ | or | https://jenkins.core.cvent.org/')
        string(name: 'target_instance_url', defaultValue: '', description: 'Destination Instance URL where JOBS need to be copied TO e.g https://svxx-jenstg-xxx.core.cvent.org/ | or | https://jenkins.core.cvent.org/')
    }
    stages {
        stage ('Copy org jobs') {
            steps {
              script {
                  withCredentials([usernamePassword(credentialsId: 'stash-credentials', passwordVariable: 'token', usernameVariable: 'username')]) {
                    sh """
                       ./copy-jenkins-jobs/copy-jobs.sh '$token' '$username'
                      """
                    }
                  }
                }
            }
        }
    }
