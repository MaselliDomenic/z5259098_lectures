
import pandas as pd
import numpy as np
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]
date_info_series = pd.Series(data = [data for _, data in date_info], index = [index for index, _ in date_info])
aud_usd_info_series = pd.Series(data = [data for _, data in aud_usd_info], index = [index for index, _ in aud_usd_info])
eur_aud_info_series = pd.Series(data = [data for _, data in eur_aud_info], index = [index for index, _ in eur_aud_info])

date_info_sorted = date_info_series.sort_index()
dates = date_info_sorted.values
print(dates)
aud_usd_info_sorted = aud_usd_info_series.sort_index()
print(aud_usd_info_sorted)
eur_aud_info_sorted = eur_aud_info_series.sort_index()
print(eur_aud_info_sorted)
dfu= pd.DataFrame({'AUD/USD': aud_usd_info_sorted, 'EUR/AUD': eur_aud_info_sorted})
dfu.index = dates
df = dfu.sort_index()
print(df)




