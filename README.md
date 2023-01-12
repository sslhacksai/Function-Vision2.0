# Function-Vision2.0

一个用python实现的绘制函数图像的科学计算器，理想效果参考 desmos 科学计算器

该项目的初衷是为无网环境提供一个可视化函数的平台。

## 使用教程

点击 Function-Vision.exe 启动程序，你可以通过直接输入函数的表达式，来得到函数的图像！

### part1 函数输入

以下为本程序支持的函数，由于本程序并未编写Latex显示，因此请确定您的表达式输入符合本程序规范，否则会出错退出:

|数学形式   |程序形式   |
|:-----------:|:----------:|
|$\pi$|pi|
|$e$|e|
|$a+b$|a+b|
|$a-b$|a-b|
|$a\times b$|a*b|
|$\frac{a}{b}$|a/b|
|$x^n$|pow(x,n)|
|$\sqrt{x}$|sqrt(x)|
|$\ln x$|log(x)|
|$\log_2 x$|log2(x)|
|$\log_{10} x$|log10(x)|
|$\log_a x$|log(x,a)|
|$e^x$|exp(x)|
|$\sin x$|sin(x)|
|$\cos x$|cos(x)|
|$\tan x$|tan(x)|
|$\arcsin x$|asin(x)|
|$\arccos x$|acos(x)|
|$\arctan x$|atan(x)|
|$\sinh x$|sinh(x)|
|$\cosh x$|cosh(x)|
|$\tanh x$|tanh(x)|
|$\|x\|$|fabs(x)|
|$\lfloor x \rfloor$|floor(x)|
|$\lceil x \rceil$|ceil(x)|
|$\gcd(a,b)$|gcd(a,b)|
|$\operatorname{lcm}(a,b)$|lcm(a,b)|
|$\sum\limits_{i=1}^{n}a_i$|sum(a1,a2,a3……an)|
|$\prod\limits_{i=1}^{n}a_i$|prod(a1,a2,a3……an)|
|$\operatorname{\frac{d}{dx}}f(x)$|dy_dx('f(x)',x)|

例如，函数 $f(x)=\operatorname{\frac{d}{dx}}(\sinh(x)e^x)+x^3$ 应输入为 dy_dx('sinh(x)*exp(x)',x)+pow(x,3)

正确输入了表达式，然后按下 <kbd>ENTER</kbd> ，函数图像就能够绘制了

### part2 视窗控制

当函数图像成功绘制的时候，你可以通过键盘控制视窗位置，以此来观察该函数任何一处的性态

|按键   |对应操作   |
|:----------:|:-----------:|
|<kbd>a</kbd>|向左移动视窗|
|<kbd>d</kbd>|向右移动视窗|
|<kbd>w</kbd>|向上移动视窗|
|<kbd>s</kbd>|向下移动视窗|
|<kbd>j</kbd>|拉伸坐标轴（视窗放大）|
|<kbd>k</kbd>|压缩坐标轴（视窗缩小）|

### part3 其他操作

|按键   |对应操作   |
|:----------:|:-----------:|
|<kbd>ESC</kbd>|退出当前函数图表，并新建图表|
|<kbd>shift</kbd>+<kbd>+</kbd>|为当前图表新增一个函数|
|输入一个点的坐标|在坐标系上描点|
|如果你是命运石之门厨且输入了暗号|恭喜你找到彩蛋！|

---


那么你已经了解了该项目的基本功能，快去试试吧！

如果发现了 bug 或者有改进的思路，请随时向我提出，感谢支持！

若要运行源码请将源码与资源放置在相同目录下

---

由于本项目绘制函数的方法是原始的描点连线法，因此在存在无极限点的函数（如 $\lfloor x \rfloor$ 或 $\tan (x)$） 时会有一定的显示方面的问题，目前尚未找到方法解决，如果有想法欢迎在讨论中提出

