# scp -i /tmp/prueba.pem -r /var/jenkins_home/workspace/pipelines-test/ ubuntu@ec2-18-216-190-103.us-east-2.compute.amazonaws.com:/home/ubuntu/main/
scp -i /tmp/prueba.pem ./scripts/deploy/publish ubuntu@44.203.185.252:/tmp/publish
ssh -i /tmp/prueba.pem  ubuntu@44.203.185.252 /tmp/publish

echo "before deploy"
echo "DEPLOY"
