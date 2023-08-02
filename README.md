# KIML(Kakao I Machine Learning) Monitoring

본 레포지토리는 국가에서 제공하는 [인공지능 고성능 컴퓨팅 자원 지원](https://aihub.or.kr/devsport/aicomputingsport/list.do?currMenu=121&topMenu=101) 중 [Kakao i Cloud](https://console.ml.kakaoicloud-kr-gov.com/)를 이용하다가 개인적으로 사용하기 위해 만든 KIML Monitoring입니다.

**개인적으로 사용하기 위해 간단하게 만들었기 때문에 원하는 기능은 수정 또는 추가를 해야할 수 있습니다.**

**아직 발표되지 않은 SDK를 직접 분석해서 만든 것으로 부족한 부분이 많을 수 있습니다.**


## 사용방법

### 1. 실행방법

- `sample_env`에서 아래 4가지에 대한 값을 추가하고 `.env`로 만들면 됩니다.
- `KIML_GPU_QUOTA` 같은 경우는 아래 예시로 넣으시면 됩니다.
    - ex) A100 80GPU(a100) 4개와 A100 MIG(a100_mig_10) 1개를 사용하는 경우
        - `KIML_GPU_QUOTA=4.14`
    - ex) A100 80GPU(a100) 2개와 A100 MIG(a100_mig_10) 1개를 사용하는 경우
        - `KIML_GPU_QUOTA=2.14`

```
KIML_ID=<kiml-id>
KIML_PW=<kiml-password>
KIML_WORKSPACE=<kiml-workspace>
KIML_GPU_QUOTA=<GPU-QUOTA>
```

- docker-compose 실행

```
docker-compose up -d
```

### 2. 실험 Submit 방법

[submit](./submit) 폴더에 있는 `main.py`와 `sample.yaml`을 참고하면 됩니다.

```
python main.py --yaml sample.yaml
```

## Preview

특별한 기능 없고 한 눈에 보고 여러 실험을 Queue에 넣어 알아서 순차적으로 제출될 수 있도록 하기 위해 매우 Simple하게 만들었습니다.  
**제출량과 실험이 적을 것으로 생각하여 Redis에서 데이터가 사라지지 않도록 해놨으니 상당히 많은 실험을 하실 경우 수정해야할 수 있습니다.**

### 1. KiML Dashboard

맨 오른쪽에 있는 Link를 통해 해당 실험 Tensorboard에 바로 접속할 수 있습니다.

![KiML](https://github.com/tony9402/kiml-monitoring/assets/30228292/1fe3f946-0aec-4d1d-9d65-5f1b5fd900d3)

### 2. Submit Dashboard

맨 오른쪽에 있는 Cancel을 통해 Pending 중인 작업을 취소할 수 있습니다.

![Submit](https://github.com/tony9402/kiml-monitoring/assets/30228292/041dfc84-30e4-4222-80ca-706ed2087200)

