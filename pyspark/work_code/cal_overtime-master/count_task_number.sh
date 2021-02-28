#!/bin/sh
JOB_NAME=$1
JOBS_BASE_DIR='/disk1/analysis/jenkins_server_secure/home/jobs'
JS_BASE_DIR='/disk1/analysis/demo/request_log_demo_online_secure/bin/mix'
JS_FILES=`cat $JOBS_BASE_DIR/$JOB_NAME/config.xml | grep run_mix.sh | sed "s/ \+/ /g" | cut -d ' ' -f 2`
TASK_COUNT=0
for JS_FILE in ${JS_FILES[*]}
do
    let TASK_COUNT=TASK_COUNT+`cat $JS_BASE_DIR/$JS_FILE | grep -o addTask | wc -l`
done
echo $TASK_COUNT
