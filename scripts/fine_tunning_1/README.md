# Fine tunning 1

O primeiro fine tunning consistiu nos seguintes hiperparâmetros:

```python
lora_config = LoraConfig(
    r=16,
    lora_alpha=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], # Modules to apply LoRA to
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
```

Além disso, a diferença entre o primeiro e o segundo fine tunning foi o learning rate. Este fine tunning teve `2e-4` de learning rate.

Para utilizar os notebooks `GerandoSQL_ModeloTunado` e `AvaliaçãoMMLU_modeloTunado`, é preciso baixar o adaptador treinado. Ele se encontra no seguinte drive (utilize uma conta do domínio do IComp):

https://drive.google.com/drive/folders/1CADgJH4JmLiwoa6Tb053JXF71F1S7lkG?usp=sharing
