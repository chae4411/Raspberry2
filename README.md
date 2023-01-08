## 0. 라즈베이파이 업데이트
``` 
sudo apt update
sudo apt upgrade
```
## 1. Repository의 GPG key를 더하기
```
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```
## 2. Repository를 더하기
```
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```
#@ 3. 프로그램 설치
```
sudo apt update
sudo apt install influxdb
```
## 3.1 프로그램 실행 전 설정
```
sudo systemctl unmask influxdb
sudo systemctl enable influxdb
sudo systemctl start influxdb
```
## 4. 데이터베이스 만들기
```
$ influx
>create database <데이터베이스이름>
확인 : show databases 
```
# Grafana Installation
## 1. Repository의 GPG key를 더하기
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
## 2. Repository를 더하기
```
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
## 3. 프로그램 설치
```
sudo apt update
sudo apt install grafana
```
## 4. 프로그램 실행
```
sudo service grafana-server start
```
## influxdb import with python
```
sudo pip3 install influxdb
```

## 라즈비안 리눅스 명령어
  - ls
  ```
    현재 경로 파일 리스트
  ```
  - cd
  ```
    디렉토리 변경
  ```
  - mkdir
  ```
    디렉토리 생성
  ```
  - pwd
  ```
    현재 디렉토리
  ```
  - ps-aux
  ```
    현재 실행중인 프로세스
  ```
  - netstat-tnl
  ```
    현재 사용중인 TCP 포트
  ```
  - ufw
  ```
    방화벽 설정
  ```
  - history
  ```
    명령어 history
  ```
