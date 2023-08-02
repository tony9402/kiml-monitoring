# KIML(Kakao I Machine Learning) Monitoring

본 레포지토리는 국가에서 제공하는 [인공지능 고성능 컴퓨팅 자원 지원](https://aihub.or.kr/devsport/aicomputingsport/list.do?currMenu=121&topMenu=101) 중 [Kakao i Cloud](https://console.ml.kakaoicloud-kr-gov.com/)를 이용하다가 개인적으로 사용하기 위해 만든 KIML Monitoring입니다.

**개인적으로 사용하기 위해 간단하게 만들었기 때문에 원하는 기능은 수정 또는 추가를 해야할 수 있습니다.**


## 사용방법

### 1. 실행방법

- `sample_env`에서 아래 3가지에 대한 값을 추가하고 `.env`로 만들면 됩니다.

```
KIML_ID=<kiml-id>
KIML_PW=<kiml-password>
KIML_WORKSPACE=<kiml-workspace>
```

- docker-compose 실행

```
docker-compose up -d
```

### 2. 실험 Submit 방법

[submit](./submit) 폴더에 있는 main.py와 sample.yaml을 참고하면 됩니다.

```
python main.py --yaml sample.yaml
```

## Preview

**TODO** 추가 예정