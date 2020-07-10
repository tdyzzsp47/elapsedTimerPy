# elapsedTimerPy
## インストール方法
```pip install elapsedTimerPy```
## 使用例
```
from elapsedTimerPy import elapsedTimer

timer = elapsedTimer.Timer()

timer.set_start()
tmp1 = [i for i in range(10000)]
timer.add_point("point1")
tmp2 = [i for i in range(10000)]
timer.set_end()
timer.print()
```

実行結果

```
==============================
start~point1
0.00043201446533203125 [s]
------------------------------
point1~end
0.0004150867462158203 [s]
------------------------------
Total
0.0008471012115478516 [s]
==============================
```
