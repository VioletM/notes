# linux

## **Run bash command with SIGHUP ignoring**
```bash
nohup my command&
```

## **Look permissions**

```bash
ls -la
```

## **Change permission recursive**

```bash
sudo chmod o+rwx -R anomaly_detection_poc/
```

## **Get all sizes of folders/files:**

```bash
du -hsc *
```

## **Get all sizes of folders**

```bash
sudo du -hs * | sort -h
```

## **Delete folder recurcively**

```bash
rm -R folder_name
```

## **Delete files by mask**

```bash
sudo find . -name '*.png' -type f -delete
```

## **Unpack .tgz or .gz**

```bash
tar zxvf backups.tgz -C /tmp/data
gzip -d file.gz
```

## **Ssh privat key gen**

у себя на машине:

ssh-keygen -t rsa

2. копируешь
содержимое ~/.ssh/id_rsa.pub

3 добавляешь
скопированный ключик в ~/.ssh/authorized_keys на сервере
