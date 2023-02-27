# Sparse Index Tracking with Sparse Models

Financial index tracking is a passive strategy in asset investment. Instead of dense asset allocation, sparse index tracking have several advantages, e.g., small transaction costs. Here, four sparse index tracking methods are impletemented, which are

- LASSO Regression
- Weighted LASSO Regression
- Least regression with MC penalty [1]
- LAIT [2]


The results of different methods are shown as below:

![](https://raw.githubusercontent.com/Gwan-Siu/Sparse_Index_Tracking/main/results/sparse_compare.png)



| Methods | Sharpe Ratio | Sortion Ratio | Calmer Ratio | Max Drawdown|
| :---------: | :---: | :---: | :---: | :---: |
| Nasdaq-100 | 0.6384 | 0.8027 | 0.6169| -0.2631|  
| LASSO | 0.7225 | 0.9167 | 0.7039 | -0.2716 |  
| WeightedLASSO | 0.7660 | 0.9672 | 0.7568 | -0.2621 |  
| MCPenalty | 0.9347 | 1.2175 | 1.0229 | -0.2489 |  
| LAIT | 0.8184 | 1.0352 | 0.7982 | -0.2632 |  


![](https://raw.githubusercontent.com/Gwan-Siu/Sparse_Index_Tracking/main/results/drawdown.png)


To do  
	- apply advanced deep learning algorithms for sparse financial index tracking  
	- further improve the deep learning-based models  

# References

[1] Zhang, Cun-Hui. "Nearly unbiased variable selection under minimax concave penalty." (2010): 894-942.  
[2] Benidis, K., Feng, Y., & Palomar, D. P. (2017). Sparse portfolios for high-dimensional financial index tracking. IEEE Transactions on signal processing, 66(1), 155-170.