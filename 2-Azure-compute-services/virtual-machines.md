# Running a python app on a VM

## Creating the VM from the CLI

First, login using `az login`.

Create the VM:
```
az vm create \
   --resource-group "resource-group-west" \
   --name "linux-vm-west" \
   --location "westus2" \
   --image "UbuntuLTS" \
   --size "Standard_B1ls" \
   --admin-username "udacityadmin" \
   --generate-ssh-keys \
   --verbose
```
Upon success, you will have a JSON response.

Open THE port 80 to allow outside traffic:
```markdown
az vm open-port \
    --port "80" \
    --resource-group "resource-group-west" \
    --name "linux-vm-west"
```

## Connecting to the VM

Get the public address of the VM from the CLI (or use the Azure Portal): 
```bash
az vm list-ip-addresses -g <RESOURCE-GROUP> -n <VIRTUAL-MACHINE-NAME>
```

Copy the app to the VM using the secure copy utility:
```bash
scp -r <SOURCE-DIR> [ADMIN-NAME]@[PUBLIC-IP]:<TARGET-DIR>
```
For example: `scp -r ./web udacityadmin@IPADDRESS:/home/udacityadmin`


Connect via SSH:
```bash
ssh [ADMIN-NAME]@[PUBLIC-IP]
```

Install Python Virtual Environment and NGNIX
```bash
sudo apt-get -y update && sudo apt-get -y install nginx python3-venv
```

## Configure NGNIX

We have to configure Nginx to redirect all incoming connections on port 80 to our app that will be running on localhost port 3000.
[_What is a proxy server?_](https://www.nginx.com/resources/glossary/reverse-proxy-server/)

By default, Nginx has a default page that is displayed. To modify it run:
```markdown
sudo unlink /etc/nginx/sites-enabled/default
```
Create a new file:
```markdown
cd /etc/nginx/sites-available
sudo vim reverse-proxy.conf
```
and add the content:
```markdown
server {
    listen 80;
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection keep-alive;
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
 }
```

Activate the directories by creating a sym link to the /sites-enabled directory:
```markdown
sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
```

Restart nginx so the changes take effect:
```markdown
sudo service nginx restart
```

## Run the app

cd to `web`

Create and activate the virtual env:
```markdown
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip in our virtual environment and install dependencies:
```markdown
pip install --upgrade pip 
pip install -r requirements.txt
```

Run the app:
```markdown
python application.py
```

In a web browser, visit the public IP address of the VM. You should see the application there :).

Type "exit" to disconnect from the VM.

## Clean up

```markdown
az group delete -n resource-group-west
```