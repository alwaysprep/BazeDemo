# Kuberenetes Demo

## 1) Istall Docker
https://docs.docker.com/get-docker/

## 2) Run a local docker registry

```posix-terminal
docker run -d -p 9000:5000 --restart=always --name registry registry:2
```

# For Mac 

## 3) using docker desktop

Go Preferences -> Kuberenetes -> Enable Kubernetes -> Apply

# For Linux

## 3) Install minikube
https://minikube.sigs.k8s.io/docs/start/

## 4) Run minikube

```posix-terminal
minikube start
```

### 5) Update cluster name to minikube

- Go WORKSPACE
- update _LOCAL_CLUSTER to "minikube"
