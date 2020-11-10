#!/bin/bash


for job_name in $(echo $org_jobs_list_to_copy | tr ',' ' '); do

    response_target=$(curl -o /dev/null -s -w "%{http_code}\n" -XGET "${target_instance_url}/job/${job_name}" -u "$username:$token")
    #To check if job exists at the target location
    if [[ $response_target -eq 302 ]]; then
        echo $job_name job exists at target location : $target_instance_url. Not doing anything!!
    elif [[ $response_target -eq 404 ]]; then
        echo $job_name job does not exist at target location : $target_instance_url
        curl -X GET "${source_instance_url}/job/${job_name}/config.xml" -u "$username:$token" -o "${job_name}.xml"
        echo Copying job config over to the target server
        curl -X POST "${target_instance_url}/createItem?name=${job_name}" -u "$username:$token" --data-binary "@${job_name}.xml" -H "Content-Type:text/xml"
        echo Copied job config successfully over to the target server
        echo Now copying master job data over to the target server.
        # code to loop over all the repositories in the project, can use rsync or scp
        rsync -avr "/home/jenkins/jobs/${job_name}/jobs/master a.yadav@sv50-jencim-001:/home/a.yadav
done