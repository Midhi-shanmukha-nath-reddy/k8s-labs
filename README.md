# k8s-labs

## Table of Contents
- [Docker Installation on Linux](#docker-installation-on-linux)
- [EKS Cluster Creation](#eks-cluster-creation)
  - [Install AWS CLI](#install-aws-cli)
  - [Install eksctl](#install-eksctl)
  - [Install kubectl](#install-kubectl)
  - [Configure AWS CLI](#configure-aws-cli)
  - [Create EKS Cluster](#create-eks-cluster)
  - [Scale Node Group](#scale-node-group)
  - [Delete EKS Cluster](#delete-eks-cluster)

## Docker Installation on Linux
To install Docker on a Linux machine, follow these steps:

1. Download Docker installation script:
    ```sh
    curl -fsSL https://get.docker.com -o get-docker.sh
    ```

2. Run the Docker installation script:
    ```sh
    sudo sh ./get-docker.sh
    ```

3. Add your user to the Docker group:
    ```sh
    sudo groupadd docker
    sudo usermod -aG docker $USER
    ```

4. Re-login to your VM to apply group changes.

5. Verify Docker installation:
    ```sh
    docker info
    ```

## EKS Cluster Creation
Follow these steps to create an EKS cluster:

### Install AWS CLI
1. Follow the instructions on the [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) to install AWS CLI.

### Install eksctl
1. Follow the instructions on the [EKSCTL Setup Guide](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html) to install `eksctl`.

### Install kubectl
1. Follow the instructions on the [Kubernetes Tools Guide](https://kubernetes.io/docs/tasks/tools/) to install `kubectl`.

### Configure AWS CLI
1. Go to AWS Console > Profile > Security credentials.
2. Create a new Access Key and copy the Secret Key (Note: This approach is fine for test/lab accounts, but not recommended for production).
3. Configure AWS CLI on your local machine:
    ```sh
    aws configure
    ```
    Enter the Access Key and Secret Key when prompted.

### Create EKS Cluster
1. Use `eksctl` to create an EKS cluster:
    ```sh
    eksctl create cluster --name hypha-dev-aws-uwst2 --version 1.28 --region us-west-2 --node-type t2.medium --nodes 3
    ```

### Scale Node Group
1. To scale up the node group, use the following command:
    ```sh
    eksctl scale nodegroup --cluster hypha-dev-aws-uwst2 --nodes 5 --name hypha-dev-app-ng
    ```

### Delete EKS Cluster
1. To delete the EKS cluster, use the following command:
    ```sh
    eksctl delete cluster --name hypha-dev-aws-uwst2 --region us-west-2
    ```

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you have any questions or need further assistance, please feel free to contact us at [your-email@example.com].

