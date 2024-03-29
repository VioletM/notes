- docker cp

```bash
docker cp convert_msgpack_to_table.py b226900c254a:/usr/mt_client/ad_runtime/convert_msgpack_to_table.py
```

- docker build

```bash
docker build -t mtclient_test -f Dockerfile.mt .
```

- docker open bash

```bash
docker exec -ti b226900c254a bash
```

- docker run

```bash
docker run -d mtclient_test
```

- run with overwriting entrypoint
```bash
docker run -it --entrypoint /bin/bash <image_name>
```

- docker with access to localhost

```bash
docker run -d --name grafana -p 3000:3000 --network="host" grafana/grafana
```

```bash
docker run -it --rm --entrypoint="/bin/bash" image_name
```

- docker-compose
```
ports:
  local_port: docker_port
```
