# wenet快速上手

> 本教程同时支持macOS M1

不需要安装，官方下载预训练模型，然后直接用我们提供的微小test data测试：

```
python recognize.py --checkpoint ./exp/20220506_u2pp_conformer_exp/final.pt --test_data data.txt --config ./exp/20220506_u2pp_conformer_exp/train.yaml --dict ./exp/20220506_u2pp_conformer_exp/units.txt --result_file a.txt
```

注意，这里不要下载任何数据集。


## 结果

```
2022-08-03 11:14:27,978 INFO BAC009S0002W0122 我认为跑步最重要的就是给我带来了身体健康
```

## 导出到torchscript

尝试trace到torchscript失败：

```
python export_jit.py --checkpoint ./exp/20220506_u2pp_conformer_exp/final.pt --config ./exp/20220506_u2pp_conformer_exp/train.yaml
```

注意，这里是trace不是script。

## 导出到onnx

其实可以简化版本，只需要Encoder，就可以实现推理。

```
python export_onnx_cpu.py --checkpoint ./exp/20220506_u2pp_conformer_exp/final.pt --config ./exp/20220506_u2pp_conformer_exp/train.yaml --chunk_size -1 --num_decoding_left_chunks -1 --output_dir weights
```

## 推理ONNX

```
python recognize_onnx.py --test_data data/data.txt --config ./exp/20220506_u2pp_conformer_exp/train.yaml --dict ./exp/20220506_u2pp_conformer_exp/units.txt --result_file a.txt --encoder_onnx weights/encoder.onnx --mode ctc_greedy_search
```

## 导出到WNNX

```
townnx -m encoder.pt -s 1x500x80,1 --moduleop wenet.transformer.attention.RelPositionMultiHeadedAttention,wenet.transformer.cmvn.GlobalCMVN
```

