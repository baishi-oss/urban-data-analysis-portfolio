# 第一周：Python 模块与数据清洗

## 学习目标

- 把入口、清洗逻辑和统计逻辑拆分到不同模块。
- 使用函数清理缺少类别或行政区的记录。
- 使用字典累计设施数量。
- 理解 `if __name__ == "__main__"`。
- 编写保留函数元信息的计时装饰器。

## 文件

- `main.py`：构造城市设施示例数据并调用统计模块。
- `facility_stats.py`：数据清洗、按类别统计和按行政区统计。
- `decorators.py`：`@timer` 装饰器练习。

```powershell
python main.py
python decorators.py
```

这一阶段建立的“读取—清洗—统计—输出”结构，后来用于南京老旧小区分析项目。
