# Simple CICD with github

pipeline
- git clone
- git build docker image
- git 


# Install docker in the agent machine
- install docker
```
sudo apt-get install docker.io
```
- verify installation
```
sudo docker run hello-world
```
- put ubuntu to the docker access group
```
sudo usermod -aG docker $USER
```
- refresh the group

```
newgrp docker
```


# using docker 
```
pipeline {
    agent {label "agent"}
    
    stages{
        stage("git clone"){
            steps{
                echo "clone the code from the github"
                git url:"https://github.com/s-4-m-a-n/30-days-of-devops-challange.git", branch:"main"
                echo "code sucessfully cloned .."
            }
        }
        stage("build"){
            steps{
                echo "build the app.."
                sh "echo $PWD"
                sh "whoami"
                echo "change director to the simple fastapi app file"
                sh "cd CICD-jenkins/simple-fastapi-app/ && docker build -t fastapi-app:latest ."
                sh "docker ps"
                echo "image build successful"
            }
        }
        stage("testing"){
            steps{
                echo "running unit testing..."
            }
        }
        
        stage("deploy"){
            steps{
                echo "deploying the code..."
                sh "docker network inspect app-network >/dev/null 2>&1 || docker network create app-network"
                sh "docker run -d --name redis --network app-network redis:latest"
                sh "docker run -p 8000:8000 --name fastapi-app --network app-network -e REDIS_HOST=redis fastapi-app"
                echo "deployment successful "                
            }
        }
    }
}
```

# Using docker compose up
```

```