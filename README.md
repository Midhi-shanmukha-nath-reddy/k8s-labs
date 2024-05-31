# k8s-labs

# Docker installation on Linux
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh 

sudo groupadd docker
sudo usermod -aG docker $USER

Re-login back into the VM
Docker info

# EKS cluster creation 
 -> install aws cli
 https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions

 -> install eksctl
 https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html

 -> install kubectl
 https://kubernetes.io/docs/tasks/tools/
 
 -> Go to AWS Console > profile > Security credentials > Create New Access key and copy Secret value (Note its not recommended, this approach is fine for test/lab accounts)
 -> on your machine or laptop where you have installed aws cli
 -> aws configure 
    enter the access key and secret key
-> eksctl create cluster --name hypha-dev-aws-uwst2 --version 1.28  --region us-west-2 --node-type t2.medium --nodes 3

# To scale up the node group 
-> eksctl scale nodegroup --cluster hypha-dev-aws-uwst2 --nodes 5 --name hypha-dev-app-ng

# To delete the EKS cluster
-> eksctl delete cluster --name hypha-dev-aws-uwst2 --region us-west-2
