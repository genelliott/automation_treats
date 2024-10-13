# Ansible Playbook Collection
Here are a collection of playbooks and roles that demonstrate different features of ansible.

## **Warning and License Notice**

**Warning:**

This Ansible playbook collection is intended for use in specific environments and configurations. It may require modifications or adjustments to suit your particular needs. **Use this collection at your own risk.** The author is not responsible for any damages or losses that may result from the use or misuse of this collection.

**License:**

This Ansible playbook collection is licensed under the BSD 3-Clause License. Please read the included LICENSE file for more details.

**Important Notes:**

* Ensure you have the necessary permissions and access to the target systems before running these playbooks.
* Review and customize the variables and configurations within the playbooks to match your specific requirements.
* Always test changes in a development or staging environment before applying them to production systems.
* Consider using Ansible Vault to securely manage sensitive information like passwords.
* Regularly update and maintain your Ansible roles to address security vulnerabilities and ensure compatibility with the latest versions of Ansible and Docker.

## Table of Contents

* docker_install.yml	Installs Docker and associated tools.
* docker_network.yml	Creates a Docker network.
* docker_run.yml	Runs Docker containers for various services (database, web, load balancer).
* docker_volume_create.yml	Creates Docker volumes for data storage.
* hostname_set.yml	Sets the system hostname.
* package_add.yml	Updates package repositories and installs common packages.
* timezone_set.yml	Sets the system timezone.
* user_add.yml	Creates users with specified passwords and groups.

* setup_infra.yml	Deploys all other roles in the collection.

# docker_install.yml

## Ansible Role for Installing Docker
This Ansible role automates the installation of Docker and associated tools on both Debian and RedHat-based Linux systems. It offers the following benefits:

* Distro-specific installation: Uses conditional statements to install Docker based on the operating system family (Debian or RedHat).
* Automatic configuration: Dynamically retrieves information like OS version and configures repositories accordingly.
* Comprehensive installation: Installs core Docker components (docker-ce, docker-ce-cli) along with container building tools (docker-buildx-plugin) and container orchestration aid (docker-compose-plugin).
(RedHat only) Enables and starts Docker service automatically.

### To use this role:

* Include this role in your playbook (roles: - docker_install).
* Ensure your system has internet connectivity.
* Run your playbook.

***Note:*** This role requires root or sudo privileges to execute.

# docker_network.yml

## Ansible Role for Creating a Docker Network
### Purpose:

This Ansible role automates the creation of a Docker network named test_local with a specified IP address range.

### Key Features:

* Conditional execution: The role only runs if the docker role is included, ensuring it's executed in the appropriate context.
* Network creation: Utilizes the docker_network module to create the test_local network.
* IPAM configuration: Sets the IP address range for the network using the ipam_config option.

### Usage:

Include this role in your playbook (roles: - docker_network).
Run your playbook.

### Benefits:

* Simplifies the creation of Docker networks.
* Ensures consistent and repeatable network configuration.
* Provides flexibility in specifying the IP address range for the network.

***Note:*** This role requires root or sudo privileges to execute and may require additional configuration or reboot depending on the Docker environment.

# docker_run.yml

## Ansible Role for Docker Container Management
This Ansible role automates the creation and configuration of various Docker containers for common services, including:

* Database: Creates a PostgreSQL container with encrypted password management using Ansible Vault.
* Web Server: Creates multiple customizable Nginx containers with volume mounts for web content.
* Load Balancer: Creates a HAProxy container with a configurable configuration file.

### Key Features:

* Conditional execution: Ensures containers are created only if the corresponding role (e.g., db) is included in the playbook.
* Dynamic configuration: Supports creating multiple Nginx containers with different ports and volumes using a loop.
* Encrypted password management: Utilizes Ansible Vault to securely store the PostgreSQL password.
* OS-specific package installation: Installs the appropriate client package (postgresql-client/postgresql) based on the operating system family (Debian/RedHat).
* Docker network connection: Connects all containers to the test_local Docker network (assumed to be created elsewhere).
* Template rendering: Uses a Jinja2 template (haproxy.cfg.j2) for the HAProxy configuration file.

### Benefits:

* Simplifies and automates Docker container deployments.
* Ensures consistent and repeatable container configurations.
* Provides flexibility for creating various service types.
* Enhances security through encrypted password management.

### Usage:

* Include this role and the required service roles (e.g., db, web, lb) in your playbook.
* Define any necessary variables for container configurations (e.g., Nginx volume mounts).
* Configure the test_local Docker network (if not already created).
* Run your playbook.

***Note:*** This role requires root or sudo privileges to execute and may require additional configuration depending on your environment (e.g., Ansible Vault setup for password encryption).

# docker_volume_create.yml

## Ansible Role for Creating Docker Volumes
### Purpose:

This Ansible role automates the creation of Docker volumes, specifically for database servers, using the Btrfs filesystem.

### Key Features:

* Conditional execution: The playbook only runs if both "db" and "docker" are included in the roles, ensuring it's executed in the appropriate context.
* Btrfs filesystem: Utilizes the Btrfs filesystem for the volumes, known for its advanced features like snapshots and copy-on-write.
* Dynamic volume creation: The playbook iterates over a list of volumes defined in the docker_volumes variable, creating each one with the specified device and Btrfs driver options.

### Prerequisites:

* The specified device (docker_volumes.device) must already be formatted with the Btrfs filesystem (e.g., using mkfs.btrfs /dev/sdb1).
* Ansible installed and configured.

### Usage:

* Define volumes: In your inventory or a separate variable file, specify the volumes you want to create under the docker_volumes variable. Example:

```yaml
docker_volumes:
  device: /dev/sdb1
  volumes:
    - database
```

* Run the playbook: Execute the playbook using ansible-playbook docker_volume_create.yml.

### Benefits:

* Simplifies volume creation for Docker containers.
* Ensures consistent and repeatable volume management.
* Leverages the benefits of the Btrfs filesystem for efficient storage.

***Note:*** For more complex volume configurations or additional features, consider exploring the full capabilities of the docker_volume module in Ansible.

# group_add.yml

## Ansible Role for Group Creation
### Purpose:

This Ansible role automates the creation of groups on the target system.

### Key Features:

* Group creation: Creates groups specified in the groups_admins variable.
* Dynamic group names: Allows for flexible group names by using a list in the groups_admins variable.

### Usage:

* Define groups: In your inventory or a separate variable file, specify the groups you want to create under the groups_admins variable.
* Run the playbook: Execute the playbook using ansible-playbook group_add.yml.

### Benefits:

* Simplifies group creation for multiple systems.
* Ensures consistent and repeatable group management.
* Provides flexibility in specifying group names.

***Note:*** This playbook requires root or sudo privileges to execute and may require additional configuration or reboot depending on the operating system.

# hostname_set.yml

## Ansible Role for Setting Hostname
### Purpose:

This Ansible role is designed to set the hostname of a system.

### Key Features:

* Dynamic hostname: The playbook uses the hostname variable to specify the desired hostname, allowing for flexibility in setting different hostnames.
* Confirmation message: Before setting the hostname, the playbook prints a message to the console indicating the new hostname.
* Hostname module: Utilizes the Ansible hostname module to modify the system's hostname.

### Usage:

* Set the hostname variable: In your inventory or a separate variable file, define the desired hostname under the hostname variable.
* Run the playbook: Execute the playbook using ansible-playbook hostname_set.yml.

### Benefits:

* Simplifies the process of setting hostnames for multiple systems.
* Ensures consistent and accurate hostname configurations.
* Provides a clear confirmation message before making changes.

***Note:*** This playbook requires root or sudo privileges to execute and may require additional configuration or reboot depending on the operating system.

# package_add.yml

## Ansible Role for Package Management
#### Purpose:

This Ansible role automates the process of updating package repositories and installing common packages on both Debian and RedHat-based Linux systems.

### Key Features:

* Distro-specific updates: Uses conditionals to update package repositories using yum for RedHat and apt for Debian.
* Package installation: Installs a list of common packages specified in the common_packages variable.
* EPEL repository: Installs the EPEL (Extra Packages for Enterprise Linux) repository on RedHat-based systems to expand the available package pool.
* Output logging: Prints the output of package updates for debugging purposes.

### Usage:

* Define common packages: In your inventory or a separate variable file, list the common packages you want to install under the common_packages variable.
* Run the playbook: Execute the playbook using ansible-playbook package_add.yml.

### Benefits:

* Simplifies package management for multiple systems.
* Ensures up-to-date package repositories.
* Provides a consistent approach to installing common packages.
* Offers flexibility in customizing the list of common packages.

***Note:*** This playbook requires root or sudo privileges to execute and may require additional configuration or reboot depending on the operating system.

# timezone_set.yml

## Ansible Role for Setting Timezone
### Purpose:

This Ansible role is designed to set the system's timezone.

### Key Features:

* Dynamic timezone: The playbook uses the timezone variable to specify the desired timezone, allowing for flexibility in setting different timezones.
* Confirmation message: Before setting the timezone, the playbook prints a message to the console indicating the new timezone.
* Timezone module: Utilizes the Ansible timezone module to modify the system's timezone.
* Crond restart: Automatically restarts the crond service (or cron on Debian) if the timezone is changed, ensuring that scheduled tasks are executed correctly in the new time zone.

### Usage:

* Set the timezone variable: In your inventory or a separate variable file, define the desired timezone under the timezone variable.
* Run the playbook: Execute the playbook using ansible-playbook timezone_set.yml.

### Benefits:

* Simplifies the process of setting timezones for multiple systems.
* Ensures accurate timekeeping and scheduling of tasks.
* Automatically restarts crond to reflect the new timezone settings.
* Provides a clear confirmation message before making changes.

***Note:*** This playbook requires root or sudo privileges to execute and may require additional configuration or reboot depending on the operating system.

# user_add.yml

## Ansible Role for User Creation
### Purpose:

This Ansible role automates the creation of users with specific passwords and group memberships. It differentiates between different levels of administrators (Level 1, Level 2, Level 3) and handles variations based on the operating system (RedHat or Debian).

### Key Features:

* User creation: Creates users with specified names, passwords, and group memberships.
* Password management: Uses the no_log option to prevent the password from being logged in the playbook output.
* Level-based administration: Distinguishes between different levels of administrators (Level 1, Level 2, Level 3) and assigns appropriate groups accordingly.
* OS-specific handling: Adapts user creation for RedHat and Debian systems to ensure compatibility.

### Usage:

* Define users: In your inventory or a separate variable file, specify the users you want to create under the users_admins, users_admins_level3_redhat, and users_admins_level3_debian variables. The format should be a dictionary with user names as keys and values containing passwords and groups.
* Run the playbook: Execute the playbook using ansible-playbook user_add.yml.

### Benefits:

* Simplifies user creation for multiple systems.
* Ensures consistent and secure user management.
* Provides flexibility for different administrative levels and operating systems.
* Protects sensitive password information by using the no_log option.

***Note:*** This playbook requires root or sudo privileges to execute and may require additional configuration or reboot depending on the operating system.
