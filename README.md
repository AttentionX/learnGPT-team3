# learnGPT - team 3

## week 1

### `test_5.py` (1) ?

> attention_has_no_notion_of_space - why?


### `test_5.py` (2) ?

> the variance_of `wei` after scale is 1 - why?

- what would happen if `wei` was not scaled with `1/sqrt(d_k)`?

hint (Vaswani et al., 2017) |
--- |
<img width="1161" alt="image" src="https://user-images.githubusercontent.com/56193069/217113424-5f969dca-73f6-4af6-b3f7-c6c5a85ba52a.png"> |




### `test_5.py` (3) ?

> self-attention mechanism - why?

- what advantage does the self-attention mechanism have over `HeadVer3` (an average of the past)?

hint 1 | hint 2 | hint 3 | hint 4
--- | --- | --- | ---
<img width="937" alt="image" src="https://user-images.githubusercontent.com/56193069/217112945-c009d74c-9efe-48b0-8a73-b7ae7f75315a.png"> |  <img width="896" alt="image" src="https://user-images.githubusercontent.com/56193069/217112961-2876727c-45af-4bde-ab1b-74faca0c0678.png"> | <img width="901" alt="image" src="https://user-images.githubusercontent.com/56193069/217112986-ea91148c-e460-4cc0-8f15-45c95e26a8ce.png"> | <img width="1235" alt="image" src="https://user-images.githubusercontent.com/56193069/217113162-49f5aab9-c21a-477c-8ba6-9a26fac593ac.png">

[hint 5](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) |
--- | 
<img width="1397" alt="image" src="https://user-images.githubusercontent.com/56193069/217113752-749cd9ef-85d7-48b7-864d-a04e229b9cc7.png"> | 


- what exactly are query, key and value? What are they for? 

hint 6 | hint 7 | hint 8 | hint 9
--- | --- | --- | ---
<img width="980" alt="image" src="https://user-images.githubusercontent.com/56193069/217114084-a8ba7312-bc6a-4649-a9a8-8f9328b1b0f9.png"> | <img width="1465" alt="image" src="https://user-images.githubusercontent.com/56193069/217114116-50ad556a-d13a-4079-b06d-c99d4dbff213.png"> | <img width="1390" alt="image" src="https://user-images.githubusercontent.com/56193069/217114137-9e8d623f-eb74-4ae5-8efb-8805d9fe20fa.png"> | <img width="1356" alt="image" src="https://user-images.githubusercontent.com/56193069/217114156-7ec0ade7-f928-42d4-9421-7abac41f954b.png">











## week 2 - `test_9.py` (Team 3)

```shell
pytest tests/test_9.py -s -vv
```

### test_layer_norm_features_dim_is_properly_normalized & test_layer_norm_mitigates_vanishing_gradient


> TODO 3-1: `BlockVer3`에서 사용할 `LayerNorm`을 구현해주세요.

테스트를 돌려보고 다음의 질문에 답해주세요.
1. `LayerNorm`을 통과한 후에는 어떤 특징이 있나요?
2. `LayerNorm`은 어떻게 기울기 소실 문제를 완화하나요?

### test_layer_norm_helps_when_network_is_deep

<img src='img/BlockVer3.png' width=250>
![img.png](img.png)

> TODO 3-2: `BlockVer3.forward`를 구현해주세요. LayerNorm을 위의 그림처럼 Multi-Head의 input, FeedForward의 input 총 2곳에 추가하시면 됩니다.

테스트를 돌려보고 다음의 질문에 답해주세요.
1. `BlockVer2`와 `BlockVer3` 중 어떤 것이 더 좋은 성능을 보이나요? 그 이유는 무엇인가요?
...

## Contributors



