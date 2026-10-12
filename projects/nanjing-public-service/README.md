# 南京老旧小区周边公共服务分析

## 项目简介

项目以南京 2024—2025 年老旧小区改造名单为基础，分析小区周边 500 米范围内六类公共服务设施的总量、结构、空间差异和潜在配套盲区。

[浏览网页项目说明](https://baishi-oss.github.io/urban-data-analysis-portfolio/projects/nanjing.html)

## 目录

```text
nanjing-public-service/
├─ data/
│  └─ analysis_base.csv       清洗后的公开分析底表
├─ figures/                   七张分析成果图
├─ notebooks/
│  └─ analysis.ipynb          可视化与统计分析
└─ path_config.py             相对路径与环境变量示例
```

## 主要分析

- 行政区之间的设施总量和类别差异。
- 全市、主城和核心区的分级空间分布。
- 六类设施构成与控制密度后的偏相关。
- 设施数量随距新街口距离变化的圈层差异。
- 设施总数极值小区及其类别构成。
- 改造批次、配套盲区、同区位优先名单和配套模式聚类。
- 区位与设施关键特征的散点矩阵诊断。

## 运行

从本项目目录或其子目录启动 Jupyter：

```powershell
pip install -r ..\..\requirements.txt
jupyter notebook notebooks\analysis.ipynb
```

Notebook 会自动向上寻找 `data/analysis_base.csv`，生成图表到 `figures`。

## API 与路径安全

- 公开分析 notebook 不需要 API 密钥。
- API 相关流程只通过环境变量读取密钥，示例见根目录 `.env.example`。
- `.env`、`API.env`、虚拟环境和编辑器配置均被 `.gitignore` 排除。
- 所有公开代码使用项目相对路径，不依赖 `C:`、`D:` 或 `E:` 等本机盘符。
- 如果真实密钥曾进入 Git 历史，应在服务商后台轮换；仅加入 `.gitignore` 不能清除历史。

## 数据口径与局限

设施数量来自地图平台 POI，不能直接代表设施质量、服务容量、真实步行可达性或居民满意度。分析结果用于学习和探索，不替代政府统计或正式规划评估。
