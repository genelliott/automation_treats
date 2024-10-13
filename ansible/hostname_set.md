# Role: hostname_set
## Execution 
### Using the hostname variable in hosts/inventory
```bash
ansible-playbook hostname_set.yml -k -K
```

Relies on hostname variable in the hosts/inventory file.  Make sure hosts/target_hosts in the playbook is set to all or a group name like so:

```yaml
# ...
  vars:
    target_hosts: linux # set to the appropriate target
```

### Setting hostname by passing the name as variable
```bash
ansible-playbook hostname_set.yml -k -K -e "hostname=web01.test.local"
```

Will set hostname to web01.test.local.  Make sure target_hosts or hosts is set to the target host.

We can also pass target_hosts as a parameter to target specific host.

```bash
ansible-playbook hostname_set.yml -k -K -e "hostname=postgres01.test.local" -e "target_hosts=rocky9-db"
```
