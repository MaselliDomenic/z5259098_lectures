from project2 import config as cfg
from project2 import zid_project2 as pj2
# Q1: Which stock in your sample has the highest average daily return for the
#     year 2020 (ignoring missing values)? The sample should include all tickers
#     included in the dictionary config.TICMAP. Your answer should include the
#     ticker for this stock.
tickers = cfg.TICKERS

tickersdf = pj2.mk_prc_df(tickers)
returnsdf = pj2.mk_ret_df(tickersdf)

avgret= {}
for t in tickers:
    avgret[t] = (pj2.get_avg(returnsdf, t, 2020))

max_key = max(avgret, key=avgret.get)
print(max_key)

# Q2: What is the annualised return for the EW portfolio of all your stocks in
# the config.TICMAP dictionary from the beginning of 2010 to the end of 2020?

portfolioreturns = pj2.get_ew_rets(returnsdf, tickers)
_20102020ret = pj2.get_ann_ret(portfolioreturns, "2010-01-01", "2020-12-31")
print(_20102020ret)

# Q3: What is the annualised daily return for the period from 2010 to 2020 for
# the stock with the highest average return in 2020 (the one you identified in
# the first question above)?

TSLAret = pj2.mk_ret_df(tickersdf).loc[:,"TSLA"]
_20102020rettsla = pj2.get_ann_ret(TSLAret, "2010-01-01", "2020-12-31")
print(_20102020rettsla)

# Q4: What is the annualised daily ABNORMAL return for the period from 2010 to 2020 for
# the stock with the highest average return in 2020 (the one you identified in
# the first question Q1 above)? Abnormal returns are calculated by subtracting
# the market return ("mkt") from the individual stock return.

TSLAretab = pj2.mk_aret_df(returnsdf).loc[:,"TSLA"]
_20102020abrettsla = pj2.get_ann_ret(TSLAretab, "2010-01-01", "2020-12-31")
print(_20102020abrettsla)