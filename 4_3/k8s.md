Create k8s objects from yaml definion

`kubectl create -f <yaml file>`

Run Pod with nginx 

`kubectl run nginx --image=nginx`

Show details about Pod

`kubectl describe pod <podname>`

Delete pod

`kubectl delete pod <podname>`

Edit already created pod

`kubectl edit pod <podname>` or apply changes in yml and then `kubectl apply -f <filename>`

Get replication controller status

`kubectl get replicationcontroller`

Get Replica Sets

`kubectl get replicasets`

If there is already pod created and you want it to have replicated without destroying it, you can use `selectors` to add additional pods. In my case I had pod created, but then i matched the labels and set replicas to 3, so replica set added only two pods.

```
mateusz@ubuntu-server:~/kube$ kubectl get replicasets
NAME       DESIRED   CURRENT   READY   AGE
nginx-rs   3         3         3       8s
mateusz@ubuntu-server:~/kube$ 
mateusz@ubuntu-server:~/kube$ kubectl get pods
NAME             READY   STATUS    RESTARTS   AGE
nginx-pod        1/1     Running   0          3m5s
nginx-rs-56qq2   1/1     Running   0          14s
nginx-rs-mn297   1/1     Running   0          14s
mateusz@ubuntu-server:~/kube$ 
```

Scale replicaset

modify yaml file and then `kubectl replace -f replicaset.yml`
or
`kubectl scale --replicas=6 -f replicaset.yml` <- change WILL NOT be reflected in replicaset.yml.
or
`kubectl scale --replicas=6 replicaset <replicaset name>` <- change WILL NOT be reflected in replicaset.yml.

Show all k8s objects

`kubectl get all`
