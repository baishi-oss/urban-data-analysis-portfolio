# 加州房价探索性数据分析

## 项目简介

使用 scikit-learn 内置 California Housing 数据集，练习特征分布检查、极端值处理、地理可视化、相关性热力图和散点图矩阵。

[浏览网页项目说明](https://baishi-oss.github.io/urban-data-analysis-portfolio/projects/california.html)

## 文件

```text
california-housing/
├─ analysis.ipynb
└─ figures/
```

## 运行

```powershell
pip install -r ..\..\requirements.txt
jupyter notebook analysis.ipynb
```

首次执行 `fetch_california_housing()` 时可能需要联网下载数据。图片输出到 `figures`。

## 处理说明

为了改善探索性图表的可读性，Notebook 过滤平均房间数大于 80、平均卧室数大于 8、人口大于 20,000 的极端记录。这一规则只用于当前可视化，不代表正式建模的最佳处理方式。

## 局限

- 当前成果不包含预测模型或模型评估。
- 相关性不代表因果关系。
- 房价目标值存在截断上限。
