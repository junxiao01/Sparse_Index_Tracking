# Sparse_Index_Tracking

Financial index tracking is a passive strategy in asset investment. Instead of dense asset allocation, sparse index tracking have several advantages, e.g., small transaction costs. Here, four sparse index tracking methods are impletemented, which are

- LASSO Regression
- Weighted LASSO Regression
- Least regression with MC penalty [1]
- LAIT [2]


The results of different methods are shown as below:

![](https://raw.githubusercontent.com/Gwan-Siu/Sparse_Index_Tracking/main/results/sparse_compare.png)



| Methods | Sharpe Ratio | Sortion Ratio | Calmer Ratio | Max Drawdown|
| :-----:| :----: | :----: | :----: | :----: | :----: |
| S&P | 0.6384 | 0.8027 | 0.6169| -0.2631|
| LASSO | 0.8055 | 1.1078 | 0.7579 | -0.4032 |
| WeightedLASSO | 0.7692 | 0.9768 | 0.7272 | -0.2824 |
| MCPenalty | 1.0422 | 1.4415 | 1.0899 | -0.3123 | 
| LAIT | 0.8184 | 1.0352 | 0.7982 | -0.2632 | 



[1] Zhang, Cun-Hui. "Nearly unbiased variable selection under minimax concave penalty." (2010): 894-942.  
[2] Benidis, K., Feng, Y., & Palomar, D. P. (2017). Sparse portfolios for high-dimensional financial index tracking. IEEE Transactions on signal processing, 66(1), 155-170.