## ECS-Standard Installation

The standard installation assumes an Internet connected VM which will be bootstrapped and become an install node. The ECS deployment will then proceed from the install node.

### Prerequisites

#### :hammer: Hardware Requirements

The installation process is designed to be performed from either a dedicated installation node. However, it is possible, if you so choose, for one of the ECS data nodes to double as the install node. The install node will bootstrap the ECS data nodes and configure the ECS instance. When the process is complete, the install node may be safely destroyed. Both single node and multi-node deployments require only a single install node.

The technical requirements for the installation node are minimal, but reducing available CPU, memory, and IO throughput will adversely affect the speed of the installation process:

- 1 CPU Core
- 2 GB Memory
- 10 GB HDD
- CentOS 7 Minimal installation (ISO- and network-based minimal installs are equally supported)



#### :evergreen_tree: Environmental Requirements

The following environmental requirements must also be met to ensure a successful installation:

- **Network:** All nodes, including install node and ECS data node(s), must exist on the same IPv4 subnet. IPv6 networking *may* work, but is neither tested nor supported for ECS Community Edition at this time.
- **Remote Access:** Installation is coordinated via SSH. However, public key authentication during the initial authentication and access configuration is not yet supported. Therefore, password authentication must be enabled on all nodes, including install node and ECS data node(s). *This is a known issue and will be addressed in a future release*
- **OS:** CentOS 7 Minimal installation (ISO- and network-based minimal installs are equally supported)



### Single Node Deployments

##### :one: Git clone the **ECS-CommunityEdition** repository.

Before data store nodes can be created, the install node must be prepared. If acquiring the software via the GitHub repository, run:

1. `cd $HOME`
2. `sudo yum install -y git`
3. `git clone https://github.com/EMCECS/ECS-CommunityEdition`.

**:two:Create deploy.yml**

1. From the `$HOME/ECS-CommunityEdition` directory, run the commmand: `cp docs/design/reference.deploy.yml deploy.yml`
2. Edit the file with your favorite editor on another machine, or use `vi deploy.yml` on the install node. Read the comments in the file and review the examples in the `examples/` directory.
3. Top-level deployment facts (`facts:`) 0. Enter the IP address of the install node into the `install_node:` field. 0. Enter into the `management_clients:` field the CIDR address/mask of each machine or subnet that will be whitelisted in node's firewalls and allowed to communicate with ECS management API.
4. Node configuration (`node_defaults:`) 0. Enter the DNS domain for the ECS installation. This can simply be set to `localdomain` if you will not be using DNS with this ECS deployment. 0. Enter each DNS server address, one per line, into `dns_servers:`. This can be what's present in `/etc/resolv.conf`, or it can be a different DNS server entirely. This DNS server will be set to the primary DNS server for each ECS node. 0. Enter each NTP server address, one per line, into `ntp_servers:`.
5. Storage Pool configuration (`storage_pools:`) 0. Enter the storage pool `name:`. 0. Enter each member data node's IP address, one per line, in `members:`. 0. Under `options:`, enter each block device reserved for ECS, one per line, in `ecs_block_devices:`. All member data nodes of a storage pool must be identical.
6. Virtual Data Center configuration (`virtual_data_centers:`) 0. Enter each VDC `name:`. 0. Enter each member Storage Pool name, one per line, in `members:`
7. Optional directives, such as those for Replication Groups and users, may also be configured at this time.
8. When you have completed the `deploy.yml` to your liking, save the file and exit the `vi` editor.
9. Move on to Bootstrapping

### Bootstrapping the Install Node (`bootstrap.sh`)

The bootstrap script configures the installation node for ECS deployment and downloads the required Docker images and software packages that all other nodes in the deployment will need for successful installation.

Once the deploy.yml file has been created, the installation node must be bootstrapped. To do this `cd` into the ECS-CommunityEdition directory and run `./bootstrap.sh -c deploy.yml`. Be sure to add the `-g` flag if building the ECS deployment in a virtual environment and the `-y` flag if you're okay accepting all defaults.

The bootstrap script accepts many flags. If your environment uses proxies, including MitM SSL proxies, custom nameservers, or a local Docker registry or CentOS mirror, you may want to indicate that on the `bootstrap.sh` command line.



###  Deploying ECS Nodes (`step1`)

Once the deploy.yml file has been correctly written and the install node rebooted if needed, then the next step is to simply run `step1`.

After the installer initializes, the EMC ECS license agreement will appear on the screen. Press `q` to close the screen and type `yes` to accept the license and continue or `no` to abort the process. The install cannot continue until the license agreement has been accepted.



### Deploying ECS Topology (`step2`)

*If you would prefer to manually configure your ECS topology, you may skip this step entirely.*

Once `step1` has completed, you may then direct the installer to configure the ECS topology by running `step2`. Once `step2` has completed, your ECS will be ready for use.