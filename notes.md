# Definition
1.Arthur Samuel(1959): Field of study that gives computers the ability to learn without being explicitly programmed.

2.Tom Mitchell(1998): A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.
### Supervised learning
	processed or labeled dataset
### Unsupervised learning
	unprocessed dataset

# First Algorithm——Linear regression(线性回归) with one variable
## The Discription of the Model
Supervised Learning: Given the "right answer" for each example in the data.

Regression Problem: Predict real-value output.

Notation:
	
	m = Number of **training examples**
	
	x's = "input" variable/features
	
	y's = "output" variable/"target" variable
	
Training Set -> Learning Algorithm -> h(hypothesis) -> input dataset and estimated value

## Cost Function
线性回归方程 -> 拟合度越高越好

平方误差代价函数
![image](https://user-images.githubusercontent.com/116483698/209258523-af83fbfb-2044-4e3c-919e-0987be92d383.png)

### while θ_0 = 0:
![image](https://user-images.githubusercontent.com/116483698/209258834-15fcfc33-a213-4781-bb0e-5f49da823586.png)
取θ_1的值，s.t. J(θ_0)最小

### while θ_0 != 0:
![image](https://user-images.githubusercontent.com/116483698/209289872-41674aad-0c87-490e-9fb1-be1a8b4079e3.png)

Contour plots(等高线图)/Contour figures(等高图像)
![image](https://user-images.githubusercontent.com/116483698/209290251-27f8ddbc-4a6b-4283-82b1-cbb6149e0cb5.png)

## Gradient descent(梯度下降法)
