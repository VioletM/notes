# Kubernetes cheatsheet

- get pods

```bash
kubectl get po -n <namespace>
```

- logs

```bash
kubectl logs -f <pod_name> -n <namespace>
```

- delete pod

```bash
kubectl delete pod <pod_name>
```

- port forward

```
kubectl port-forward apm-server-apm-server-54d8cb6db4-dfk9c 8899:8200 -n elastic &
```
