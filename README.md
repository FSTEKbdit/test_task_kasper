# prometheus-task
test task for Kasper

# Структура: 
 ### 1. Описание основного задания
 ### 2. Описание бонусного задания с контейнером
 
<br>
<br>

### Настройка системы (общая для всех заданий)
1. С официального сайта VirtualBox (https://www.virtualbox.org/) скачать VBox и настроить (там графический интерфейс, должно быть все понятно)
2. С официального сайта дистрибутива AlmaLinux (https://almalinux.org/get-almalinux/) скачать образ AlmaLinux-9
3. В VBox нажимаем **"Создать"** и в поле **"Образ ISO"** выбираем образ, который только что скачали. Далее настраиваем ВМ через графический интерфейс. Даем имя **"Target"**
4. После этого выключаем ВМ. В VBox выбираем нашу ВМ -> **"Настроить"** -> **"Сеть"** и у 1-го адаптера **"Тип подключения"** ставим **"Сетевой мост"**. Жмем **ОК**.
5. **ПКМ** по нашей ВМ -> **"Клонировать"**. В секции **"Политика MAC-адреса"** выбираем **"Сгенерировать новые MAC-адреса"**. Называем **"Controller"** и все принимаем.
6. Запускаем обе ВМ. В Target в терминале пишем ***'ip a'*** и копируем **IPv4-адрес**, который указан в интрефейсе enp0s3
7. На Controller устанавливаем **Ansible**. Для этого сначала выпоняем ***'sudo yum update'***, затем ***'sudo yum install -y epel-release'***. После выполняем команды из документации: https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-fedora-linux (именно из секции для **Fedora**)
8. Скачиваем на Controller роли и плейбуки ansible. В терминале выполняем ***'sudo curl -L --compressed https://github.com/FSTEKbdit/test_task_kasper/archive/refs/heads/main.tar.gz | sudo tar -xzf -'***. И переходим в директорию **"ansible"** - ***'cd ansible'***.
9. На **Controller** редактируем файл **inventory** - ***'vi inventory.ini'***. Необходимо в **ansible_host** заменить установленный там IP-адрес на адрес **Target**. Также в **ansible_password** установить пароль для ***root'а*** на хосте **Target**.

<br>

## Основное задание
1. На **Controller** выполняем ***'ansible-playbook playbook.yml -i inventory.ini'***.
2. Переходим на хост **Target** и выполняем ***'curl http://localhost:8080'***. Видим вывод нашего веб-сервиса на **Prometheus**, в последней строчке будет **"Тип хоста"** - **Virtual Machine**. Также можем посмотреть, что он работает как **служба systemd**. Для этого выполним ***'sudo systemctl status prometheus.service'***, в выводе увидим, что она **active** и **enable**.

<br>

## Первое бонусное задание с контейнером
1. На **Controller** выполняем ***'ansible-playbook playbook_docker.yml -i inventory.ini'***.
2. Переходим на хост **Target** и выполняем ***'curl http://localhost:8080'***. Видим вывод нашего веб-сервиса на **Prometheus**, в последней строчке будет **"Тип хоста"** - **Container**.

<br>

## Второе бонусное задание с Terraform
1. На вашу машину, где у вас стоит VBox, установить Terraform и Vagrant. Сейчас из-за санкций с этим проблемы, но в VPN/Proxy это возможно.
2. Также установить Vagrant box для AlmaLinux 9.
3. Скопировать и разархивировать репозиторий https://github.com/FSTEKbdit/test_task_kasper/archive/refs/heads/main.zip
4. Из директории **terraform/terraform-provider-vagrant/** репозитория скопировать бинарь **terraform-provider-vagrant.exe** в директорию **C:\providers\vagrant\\**
5. Перейти в директрию terraform ***'cd terraform'*** на основном хосте (где устновлен VBox). И выполнить ***'terraform apply --auto-approve'***
6. Когда все выполнится, перейти на **Controller** в директорию ansible ***'cd ansible'***, вернуть **inventory.ini** к первоначальному состоянию (какой он был на github). И выполнить ***'ansible-playbook playbook_docker.yml -i inventory.ini'***.
7. Далее перейти на нашу созданную terraform'ом ВМ ***'ssh 127.0.0.1@vagrant'***. Делаем отпечаток (пишем **yes**) и вводим пароль **vagrant**. На ней выполняем ***'curl http://localhost:8080'***. Видим вывод нашего веб-сервиса на **Prometheus**, в последней строчке будет **"Тип хоста"** - **Virtual Machine**. Также можем посмотреть, что он работает как **служба systemd**. Для этого выполним ***'sudo systemctl status prometheus.service'***, в выводе увидим, что она **active** и **enable**.

<br>

**Все**
