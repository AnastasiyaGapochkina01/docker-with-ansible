# Docker container as systemd unit with ansible

```
ansible-vault encrypt_string "you-token-here" --name "dockerhub_token"
ansible-playbook -i inventory/inventory main.yaml --ask-vault-pass
```