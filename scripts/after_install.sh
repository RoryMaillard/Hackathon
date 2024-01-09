#!/bin/bash

echo "Logging in to Amazon ECR..."
docker login --username AWS --password $(aws ecr get-login-password --region eu-north-1) 133470028655.dkr.ecr.eu-north-1.amazonaws.com
echo "Logged in to Amazon ECR successfully."

echo "Pulling image from Amazon ECR"
docker pull 133470028655.dkr.ecr.eu-north-1.amazonaws.com/apiculture_image:latest
echo "Pulled image from Amazon ECR successfully."