import numpy
import pandas
from spsspro.algorithm import statistical_model_analysis
#生成案例数据
data = pandas.DataFrame({
    "A": numpy.random.random(size=20)
})
#时间序列分析(ARIMA)，输入参数详细可以光标放置函数括号内按shift+tab查看，输出结果参考spsspro模板分析报告
result = statistical_model_analysis.arima_analysis(data=data, p=0, d=0, q=0, forecast_num=10)
print(result)