Install webserver on EC2 using Ansible

Step1 : Create EC2 Instance
ansible-playbook ec2-instance.yml 

Step2: Install Webserver and configure , enable SSL , Http to https redirect
 
ansible-playbook webserver.yml --user=ubuntu -i inventory

Note: Placing pem file manually in folder
