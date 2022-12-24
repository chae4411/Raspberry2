# 아두이노 조도센서 프로그램

```c
int cds = A0;
int LED = 9;

void setup() {
  Serial.begin(9600);
  pinMode(cds,INPUT);
}

void loop() {
  cds = analogRead(A0);
  Serial.println(cds);
  delay(500);
}

```

## 라즈베리파이 미들웨어 (아두이노 시리얼 -> 라즈베리파이 influxDB)
```
lux.py
```
