# Role: timezone_set
## Execution 
### Using the timezone variable in hosts/inventory
```bash
ansible-playbook timezone_set.yml -k -K
```

Relies on timezone variable in the hosts/inventory file.  Make sure hosts/target_hosts in the playbook is set to all or a group name like so:

```yaml
# ...
  vars:
    target_hosts: linux # set to the appropriate target
```

### Setting timezone by passing the name as variable
```bash
ansible-playbook timezone_set.yml -k -K -e "timezone=Australia/Sydney"
```

Will set timezone to web01.test.local.  Make sure target_hosts or hosts is set to the target host.

We can also pass target_hosts as a parameter to target specific host.

```bash
ansible-playbook timezone_set.yml -k -K -e "timezone=Australia/Brisbane" -e "target_hosts=rocky9-db"
```
