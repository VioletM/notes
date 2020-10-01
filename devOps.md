# devOps

## **Активация окружения на конде**

```bash
source activate idp
```

## **White theme**

```bash
!jt -r
```

## **Dark theme**

```bash
!jt -t onedork -fs 95 -tfs 11 -nfs 115 -cellw
70% -T -N -f source
```

## **Jupyter run on server**

```bash
jupyter notebook --no-browser --port=8889
ssh **-**N **-**f **-**L localhost**:**YYYY**:**localhost**:**XXXX remoteuser**@**remotehost
#open browser on http://localhost:YYYY
```

## **Code to run prometheus and grafana each in docker container**

```bash
docker pull prom/prometheus
docker run -d --name prometheus --network="host" -p 9090:9090 -v <PATH_TO_PROJECT_with_YML>:/opt/<PROJECT> prom/prometheus --config.file=/opt/<PROJECT>/prometheus.yml
# prometheus is available on localhost:9090
```

```bash
docker pull grafana/grafana
docker run -d --name grafana -p 3000:3000 --network="host" grafana/grafana
# grafana is available on localhost:3000
```
## **MLFlow**

https://towardsdatascience.com/setup-mlflow-in-production-d72aecde7fef
