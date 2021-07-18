
# Trigo Project

This project deploys simple web server that written in flask - micro web framework written in Python.
The web server serve 3 links of 3 different deployments in k8s cluster that will be created during this project.
* http://your_host:8080/prod/redis/config - redis prod configuration (service A)
* http://your_host:8080/prod/redis/config - redis dev configuration (service A)
* http://your_host:8080/prod/nginx/config nginx prod configuration (service B)

## Prerequisites

- K8s cluster (minikube/other tool that let you deploy k8s cluster)
- all packages that mention in requirements.txt file
- access to kubeconfig file
- kubectl


## Clone Repo

To install this repo 

```bash
$ git clone https://github.com/trigodevops/test_repo.git
$ cd test_repo
```

## Creating the k8s deployments

```bash
# creating namespaces
$ kubectl create ns nginx-prod
$ kubectl create ns redis-prod
$ kubectl create ns redis-dev
```

```bash
# creating configmaps that will be our deployment configuration
$ kubectl apply -f ./Apps/redis/config/prod/redis-config-prod.yaml -n redis-prod
$ kubectl apply -f ./Apps/redis/config/dev/redis-config-dev.yaml -n redis-dev
$ kubectl apply -f ./Apps/redis/config/dev/nginx-config-dev.yaml -n nginx-prod
```

```bash
# creating our deployments
$ kubectl apply -f ./Apps/redis/config/redis-deployment-prod.yaml -n redis-prod
$ kubectl apply -f ./Apps/redis/config/redis-deployment-dev.yaml -n redis-dev
$ kubectl apply -f ./Apps/nginx/nginx-deployment.yaml -n nginx-prod
```
## Checking your deployments
```bash
#check all your deployments are in 'Running' state with this command:
$ kubectl get deployments -n redis-prod
$ kubectl get deployments -n redis-dev
$ kubectl get deployments -n nginx-prod
```

## Start the web server
```bash
$ flask run -h <your_host> -p 8080
```

## Access to your web server
```bash
$ curl -GET "http://your_host:8080/prod/redis/config" 
$ curl -GET "http://your_host:8080/dev/redis/config"
$ curl -GET "http://your_host:8080/prod/nginx/config"
```

## Upgrade App version for nginx and redis

``` bash
we will upgrade our application version with newer images
$ kubectl set image deployment/redis redis=redis/5.0.4 -n redis-dev
$ kubectl set image deployment/nginx-prod nginx-prod=nginx:1.20.1 -n nginx-prod
```


## Update configuration and verify of redeploying app and updating the links.

``` bash
first lets update the configmap for these applications
$ kubectl edit configmap nginx-config-prod -n nginx-dev
change the 'worker_connections: 10240' and save the changes
$ kubectl edit configmap redis-config-dev -n redis-dev
change the 'MEMORYFILED' and save the changes
```

``` bash
redeploy our applications 
$ kubectl rollout restart nginx -n nginx-prod
$ kubectl rollout restart deployment redis-dev -n redis-dev
```

``` bash
verify new configurations
$ kubectl exec -n redis-dev -it <redis_pod_name> -- redis-cli
$ CONFIG GET lua-time-limit
```

``` bash
verify The links are updated 
$ curl -GET "http://your_host:8080/dev/redis/config"
$ curl -GET "http://your_host:8080/prod/nginx/config"
```
