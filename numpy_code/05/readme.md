作为NumPy用户，我们有时会发现自己在金融计算或信号处理方面有一
些特殊的需求。幸运的是， NumPy能满足我们的大部分需求。本章将讲述
NumPy中的部分专用函数。
本章涵盖以下内容：
 排序和搜索；
 特殊函数；
 金融函数；
 窗口函数。

NumPy提供了多种排序函数，如下所示：
 sort函数返回排序后的数组；
 lexsort函数根据键值的字典序进行排序；
 argsort函数返回输入数组排序后的下标；
 ndarray类的sort方法可对数组进行原地排序；
 msort函数沿着第一个轴排序；
 sort_complex函数对复数按照先实部后虚部的顺序进行排序。
在上面的列表中， argsort和sort函数可用来对NumPy数组类型进行排序。


NumPy中有很多金融函数，如下所示。
 fv函数计算所谓的终值（future value），即基于一些假设给出的某个金融资产在未来某一
时间点的价值。
 pv函数计算现值（present value），即金融资产当前的价值。
 npv函数返回的是净现值（net present value），即按折现率计算的净现金流之和。
 pmt函数根据本金和利率计算每期需支付的金额。
 irr函数计算内部收益率（internal rate of return）。内部收益率是是净现值为0时的有效利
率，不考虑通胀因素。
 mirr函数计算修正后内部收益率（modified internal rate of return），是内部收益率的改进
版本。
 nper函数计算定期付款的期数。
 rate函数计算利率（rate of interest）。