# scp -i /tmp/remote-key -r /var/jenkins_home/workspace/pipelines-test/ remote_user@remote-host:/home/remote_user/
# scp -i /tmp/remote-key ./scripts/deploy/publish remote_user@remote-host:/tmp/publish
# ssh -i /tmp/remote-key  remote_user@remote-host /tmp/publish

echo "DEPLOY"