from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

namespace = "argocd"   # change your namespace

core_api = client.CoreV1Api()
metrics_api = client.CustomObjectsApi()

# Get pod status
pods = core_api.list_namespaced_pod(namespace)

# Get pod metrics
metrics = metrics_api.list_namespaced_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    namespace=namespace,
    plural="pods"
)

# Convert metrics to dictionary for quick lookup
pod_metrics = {}
for item in metrics["items"]:
    pod_metrics[item["metadata"]["name"]] = item["containers"]

for pod in pods.items:
    pod_name = pod.metadata.name
    status = pod.status.phase

    print(f"\nPod: {pod_name}")
    print(f"Status: {status}")

    if pod_name in pod_metrics:
        for container in pod_metrics[pod_name]:
            cpu = container["usage"]["cpu"]
            memory = container["usage"]["memory"]

            print(f"Container: {container['name']}")
            print(f"CPU Usage: {cpu}")
            print(f"Memory Usage: {memory}")
    else:
        print("Metrics not available")