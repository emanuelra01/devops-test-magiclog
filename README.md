# MagicLog DevOps Exercise

## Intro

Our team requires an incredible new member to help us build the Devops process according to the
needs of our IT area.

## Get your environment ready

You'll need:

1. Launch when a change is accepted in the main branch.
2. Build the image
3. Upload it to an image repository
4. Deploy it to some cloud service, for example to an ECS or Azure Container Apps
   cluster, or a virtual machine (EC2, Azure Virtual Machine) or to Kubernetes (AKS, EKS)
5. Upload all files to a cloud repository

### Attention !!!

**First you must create the infrastructure ECR and ECS, otherwise Github actions will send an error.**

**You should have installed aws client, curl and terraform**

**You will have to configure your aws profile dev**
Inside your file ~/.aws/config

[profile dev]
region = us-east-1
output = json

Inside your file ~/.aws/credentials

[dev]
aws_access_key_id = XXXX
aws_secret_access_key = XXXX

**You will need to create the ECR and ECS infrastructure**

**ECR creation**
Inside your directory ./terraform/dev-ecr/  run the following commands:

terraform init
terraform plan
terraform apply

**ECS creation**
Inside your directory ./terraform/dev-ecs/  run the following commands:

terraform init
terraform plan
terraform apply

**Github actions work on branches main, feature/create-**

**Commands to test the ECS service**
curl -X POST http://ECS Public IP:5000/birthday -H 'Content-Type: application/json' -d '{"name": "Pruebas test", "date":"1990-01-18"}'