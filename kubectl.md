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
