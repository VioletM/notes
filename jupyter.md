## Kill jupyter server
```bash
jupyter notebook list # shows the running notebooks and their port-numbers
                      # (for instance: 8080)
lsof -n -i4TCP:[port-number] # shows PID.
kill -9 [PID] # kill the process.
```
