# learnGPT - team 3

## week 1

### `test_5.py` (1) ?

> attention_has_no_notion_of_space - why?


### `test_5.py` (2) ?

> the variance_of `wei` after scale is 1 - why?

- what would happen if `wei` was not scaled with `1/sqrt(d_k)`?


### `test_5.py` (3) ?

> self-attention mechanism - why?

- what advantage does the self-attention mechanism have over `HeadVer3` (an average of the past)?
- illustrate what query, key and value are for with examples

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



