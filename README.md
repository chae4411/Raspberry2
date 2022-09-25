# 1. Repository의 GPG key를 더하기
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
# 2. Repository를 더하기
```
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
# 3. 프로그램 설치
```
sudo apt update
sudo apt install grafana
```
# 4. 프로그램 실행
```
sudo service grafana-server start
```
# influxdb import with python
```
sudo pip3 install influxdb
```
