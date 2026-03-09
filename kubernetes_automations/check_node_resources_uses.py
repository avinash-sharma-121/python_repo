from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Core API
core_api = client.CoreV1Api()

# Custom metrics API
metrics_api = client.CustomObjectsApi()

nodes = core_api.list_node()

metrics = metrics_api.list_cluster_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    plural="nodes"
)

for item in metrics["items"]:
    name = item["metadata"]["name"]
    cpu = item["usage"]["cpu"]
    memory = item["usage"]["memory"]

    print(f"Node: {name}")
    print(f"CPU Usage: {cpu}")
    print(f"Memory Usage: {memory}")
    print("--------------------")