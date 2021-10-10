# Docker container as systemd unit with ansible

Запускается с кастомным ${service_name}.yaml inventory для каждого сервиса. В нем описаны переменные для docker run (имя контейнера, image, порты, etc)

В шаблоне ${service_name} описаны энвы для контейнера (DOCKER_IMAGE для того чтобы релоадить конфиг и рестартовать контейнер, если изменился только image)

```
ansible-vault encrypt_string "${you-token-here}" --name "dockerhub_token"
ansible-playbook -i inventory/${service_name}.yaml main.yaml --ask-vault-pass
```