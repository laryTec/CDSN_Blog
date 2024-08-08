# 項目名稱

基於 Django 搭建的 Blog 網頁

## 目錄

- [安裝](#安裝)
- [Docker](#docker)

## 安裝

1. GitHub：
   ```bash
   git clone https://github.com/laryTec/CDSN_Blog.git

   cd CDSN_Blog
2. 資料庫遷移：
   ```bash
   python manage.py makemigrations

   python manage.py migrate

3. 執行：
   ```bash
   python manage.py runserver

## Docker

 ### Pull Image

```bash
docker pull mysql:8.0
```

 ### Check config

```bash
docker run --rm mysql:8.0 mysql --help | grep my.cnf
```

***

### Windows

```bash
mkdir D:\docker\mysql\conf
mkdir D:\docker\mysql\data
```

copy config to local：

> Windows D:\docker\mysql

```bash
set LOCAL_DOCKER_MYSQL_PATH=D:\docker\mysql\conf
docker run -d mysql:8.0 > temp_container_id.txt
set /p DOCKER_MYSQL_TMP=<temp_container_id.txt
docker cp %DOCKER_MYSQL_TMP%:/etc/my.cnf %LOCAL_DOCKER_MYSQL_PATH%\conf
docker stop %DOCKER_MYSQL_TMP%
docker rm %DOCKER_MYSQL_TMP%
del temp_container_id.txt
```

### run container

```bash
set LOCAL_DOCKER_MYSQL_PATH=D:\docker\mysql
docker run -d ^
-p 3306:3306 ^
--name blog_mysql ^
-e MYSQL_ROOT_PASSWORD=root ^
-v %LOCAL_DOCKER_MYSQL_PATH%\conf\my.cnf:/etc/my.cnf ^
-v %LOCAL_DOCKER_MYSQL_PATH%\data:/var/lib/mysql/ ^
mysql:8.0
```

***

### Mac

copy config to local：

> MacOS /Users/docker/mysql

```bash
LOCAL_DOCKER_MYSQL_PATH=/Users/docker/mysql \
DOCKER_MYSQL_TMP=`docker run -d mysql:8.0` \
&& docker cp $DOCKER_MYSQL_TMP:/etc/my.cnf $LOCAL_DOCKER_MYSQL_PATH/conf \
&& docker stop $DOCKER_MYSQL_TMP \
&& docker rm $DOCKER_MYSQL_TMP
```

 ### Run container

```bash
LOCAL_DOCKER_MYSQL_PATH=/Users/docker/mysql \
&& docker run -d \
-p 3306:3306 \
--name blog_mysql \
-e MYSQL_ROOT_PASSWORD=root \
-v $LOCAL_DOCKER_MYSQL_PATH/conf/my.cnf:/etc/my.cnf \
-v $LOCAL_DOCKER_MYSQL_PATH/data:/var/lib/mysql/ \
mysql:8.0
```