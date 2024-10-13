# Role: user_add
## Execution 

```bash
ansible-playbook user_add.yml -k -K
```

### Adding User to a specific host

```bash
ansible-playbook user_add.yml -k -K -e "target_hosts=rocky9-db"
```
