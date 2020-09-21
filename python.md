## **Pandas display max cols, rows**

```python
pd.set_option("display.max_columns", 999)
pd.set_option("display.max_rows", 999)
```

## **plt tricks**

```python
fig, ax = plt.subplots(figsize=(width, height)) 

plt.xticks(rotation='vertical')
```
    
 ## **Telegrambot Alert**

```python
import requests

def telegram_alert(message='Finished', key='xxxxxxx'):
    
    params = (
        ('key', key),
        ('message', message),
    )

    response = requests.get('https://alarmerbot.ru/', params=params)
    if response.content!=b'OK':
        raise RunTimeException(response)
```

## Zombie killing

```python
try:
    fun_with_n_jobs(n_jobs=16)
except BaseException as e:
    while os.waitpid(-1, os.WNOHANG) != (0, 0):
        print(f"Zombie killed")
        print('ERROR!')
        print(e)
```

## Reimport module

```python
import importlib
importlib.reload(module)
```

## Logging

```python
import logging
import sys
logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)-15s [%(name)s::%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler('./training_log.txt')
            ]
        )
```

## Pyenv

```bash
pyenv install -v 3.6.8
pyenv versions
pyenv uninstall nsi-env
pyenv virtualenv <python_version> <environment_name>
```
