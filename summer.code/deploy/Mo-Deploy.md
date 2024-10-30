### Pre-conditions

Before starting, ensure the following environment setup is ready:

- A Kubernetes cluster environment and S3 environment that meet the required resources.
- A client machine that can connect to the Kubernetes cluster.
- The client machine should have Helm and kubectl installed, with a configured kubeconfig file that allows access to the cluster, including permissions to deploy Helm charts and install CRD resources.
- Access to the internet for resources like github.io, hub.docker.com, etc. If internet access is not available, provide a private image repository to upload relevant images, and update the image repository address to this private repository in the MatrixOne cluster YAML definition.
- Cluster nodes should be able to access the object storage, including resolving the object storage domain.

**Note**: Unless specified otherwise, all operations below are executed on the client machine.

### Installing MatrixOne-Operator

[MatrixOne Operator](https://github.com/matrixorigin/matrixone-operator) is an independent software tool for deploying and managing MatrixOne clusters on Kubernetes. You can choose to perform an online or offline deployment.

Follow these steps to install MatrixOne Operator on `master0`. We will create a dedicated namespace `matrixone-operator` for the Operator.

1. Add the matrixone-operator repository to Helm:

   ```bash
   helm repo add matrixone-operator https://matrixorigin.github.io/matrixone-operator
   ```

2. Update the repository:

   ```bash
   helm repo update
   ```

3. Check the available MatrixOne Operator versions:

   ```bash
   helm search repo matrixone-operator/matrixone-operator --versions --devel
   ```

4. Install MatrixOne Operator with the specified version:

   ```bash
   helm install matrixone-operator matrixone-operator/matrixone-operator --version <VERSION> --create-namespace --namespace matrixone-operator
   ```

   **Note**: The `VERSION` parameter specifies the MatrixOne Operator version, such as `1.0.0-alpha.2`.

5. After installation, verify the installation status using the following command:

   ```bash
   kubectl get pod -n matrixone-operator
   ```

### Deploying MatrixOne

Customize the YAML file for the MatrixOne cluster by creating a configuration file, `mo.yaml`(See the example).

### Connecting to the MatrixOne Cluster

To connect to the MatrixOne cluster, you need to forward the corresponding service port to the MatrixOne node. The following is a guide to using `kubectl port-forward` to connect to the MatrixOne cluster:

- **Local Access Only**:

  ```bash
  nohup kubectl port-forward -nmo svc/svc_name 6001:6001 &
  ```

- **Allow Access from a Specific Machine or All Machines**:

  ```bash
  nohup kubectl port-forward -nmo --address 0.0.0.0 svc/svc_name 6001:6001 &
  ```

After configuring **local access** or **access from a specific machine or all machines**, you can use the MySQL client to connect to MatrixOne:

```
bashCopy code# Use the 'mysql' command-line tool to connect to the MySQL service
# Use 'kubectl get svc/svc_name -n mo -o jsonpath='{.spec.clusterIP}' ' to obtain the Cluster IP address of the service in Kubernetes
# '-h' specifies the hostname or IP address of the MySQL service
# '-P' specifies the port of the MySQL service, in this case, 6001
# '-uroot' logs in with the root user
# '-p111' indicates the initial password is 111
mysql -h $(kubectl get svc/svc_name -n mo -o jsonpath='{.spec.clusterIP}') -P 6001 -uroot -p111
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 163
Server version: 8.0.30-MatrixOne-v1.1.1 MatrixOne

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Once you see `mysql>`, the connection to the distributed MatrixOne cluster has been successfully established.

