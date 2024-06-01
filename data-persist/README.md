# Data Persistance

cd data-persist

# Building  and push Docker image, if your building Docker image on linux/windows --platform can be ignored 

docker buildx build --no-cache  --platform linux/amd64 -t  dockerreponame/hypha-data-demo:v1 .

docker login 

docker push dockerreponame/hypha-data-demo:v1

k create ns data-apps

# to install Drivers of EBS-CSI 

helm repo add aws-ebs-csi-driver https://kubernetes-sigs.github.io/aws-ebs-csi-driver
helm repo update
helm upgrade --install aws-ebs-csi-driver aws-ebs-csi-driver/aws-ebs-csi-driver \
  --namespace kube-system \
  --set image.repository=602401143452.dkr.ecr.us-west-2.amazonaws.com/eks/aws-ebs-csi-driver


# make sure attach policy to the ec2 attached IAM roles in the aws 

Go to Services -> IAM
Create a Policy
Select JSON tab and copy paste the below JSON

Name: EBS_CSI_Driver
Description: Policy for eks nodes to access EBS
Click on Create Policy


Get the IAM role Worker Nodes using and Associate this policy to that role

# Get Worker node IAM Role ARN
kubectl -n kube-system describe configmap aws-auth

# from output check rolearn
arn:aws:iam::xxxxxxx:role/eksctl-hypha-dev-aws-uwst2-nodegro-NodeInstanceRole-Gv8RW5o3
-> Go to Services -> IAM -> Roles - Search for role with name hypha-dev-aws-uwst2-nodegroup and open it - Click on Permissions tab - Click on Attach Policies - Search for EBS_CSI_Driver and click on Attach Policy


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateSnapshot",
                "ec2:AttachVolume",
                "ec2:CreateVolume",
                "ec2:DeleteSnapshot",
                "ec2:DeleteVolume",
                "ec2:DetachVolume",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeInstances",
                "ec2:DescribeSnapshots",
                "ec2:DescribeTags",
                "ec2:DescribeVolumes",
                "ec2:DescribeVolumesModifications",
                "ec2:ModifyVolume"
            ],
            "Resource": "*"
        }
    ]
}


k get po -n kube-system
k apply -f storageclass.yaml
k apply -f deployment.yaml -n data-apps
k apply  -f pvc.yaml -n data-apps
k apply -f service.yaml -n data-apps
k apply -f ../flask-app/cm.yaml -n data-apps
k apply -f ../flask-app/secret.yaml -n data-apps
k get po -n data-apps
k get pvc -n data-apps
k get svc -n data-apps

###