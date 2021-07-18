#!/usr/bin/python3
from flask import Flask
from kubernetes import client, config
from kubernetes.config.kube_config import ConfigException

SERVICE_REDIS_PROD_NAMESPACE = "redis-prod"
SERVICE_REDIS_PROD_LABEL = "environment=prod"
SERVICE_REDIS_DEV_NAMESPACE = "redis-dev"
SERVICE_REDIS_DEV_LABEL = "environment=dev"
SERVICE_NGINX_PROD_NAMESPACE = "nginx-prod"
SERVICE_NGINX_PROD_LABEL = "environment=prod"

app = Flask(__name__)


def create_k8s_instance():
    """
    This function load the kubeconfig file from ~/root/.kube/config and use it to connect to the k8s cluster
    :return: kubernetes.client.api.core_v1_api.CoreV1Api Object
    """
    try:
        config.load_kube_config()
    except ConfigException:
        return "Make sure you have the kubeconfig file in ~/.kube/config"
    return client.CoreV1Api()


@app.route("/prod/redis/config")
def service_redis_prod():
    """
    This function by using label and namespace filter find the configuration of redis prod deployment
    :return: dict object of the prod configuration data of redis
    """
    try:
        return K8S_INSTANCE.list_namespaced_config_map(namespace=SERVICE_REDIS_PROD_NAMESPACE,
                                                       label_selector=SERVICE_REDIS_PROD_LABEL).items[0].data
    except IndexError:
        return "You dont have configmap with this label or in this namespace"
    else:
        return "Something went wrong check your connection"


@app.route("/dev/redis/config")
def service_redis_dev():
    """
    This function by using label and namespace filter find the configuration of redis dev deployment
    :return: dict object of the dev configuration data of redis
    """
    try:
        return K8S_INSTANCE.list_namespaced_config_map(namespace=SERVICE_REDIS_DEV_NAMESPACE,
                                                       label_selector=SERVICE_REDIS_DEV_LABEL).items[0].data
    except IndexError:
        return "You dont have configmap with this label or in this namespace"
    else:
        return "Something went wrong check your connection"


@app.route("/prod/nginx/config")
def service_nginx_dev():
    """
    This function by using label and namespace filter find the configuration of nginx prod deployment
    :return: dict object of the prod configuration data of nginx
    """
    try:
        return K8S_INSTANCE.list_namespaced_config_map(namespace=SERVICE_NGINX_PROD_NAMESPACE,
                                                       label_selector=SERVICE_NGINX_PROD_LABEL).items[0].data
    except IndexError:
        return "You dont have configmap with this label or in this namespace"
    else:
        return "Something went wrong check your connection"


K8S_INSTANCE = create_k8s_instance()
