#from youtube - https://www.youtube.com/watch?v=gRRocTAtZm8
#github - kjam -
import time
t1 =time.process_time_ns()
print(t1)
from dask.distributed import Client

# client = Client(n_workers=2, threads_per_worker=2, memory_limit='1GB')
# client
if __name__ == '__main__':
    client = Client(processes=False)

from dask import dataframe as ddf
# da = array.random.binomial(100, .3, 1000,chunks=(100))
# print(da.size)
# print(da[:2])
# print(da.npartitions)#doing partition based on chunksize
# print(da[:1100].chunks)
# # print(da.min().visualize())
# print(da.min().compute())

headers_revdtc = ["REV_ITEM",
"REV_STORE",
"REV_DTC_NUM",
"REV_DTCE_NUM",
"REV_TOTPLNS",
"REV_CUR_FACE",
"REV_CUR_PRES",
"REV_CUR_FILL",
"REV_CUR_CAP",
"REV_CHKOUT",
"REV_DEPT",
"REV_CATG",
"REV_REC_CRDTE",
"REV_REC_LUDTE",
"REV_PLNBUS",
"REV_CUR_DISP_FACE",
"REV_P`LANOGRAM",
"REV_ITEM_SEQ",
"REV_ITEM_SEQ_VER",
"FILLER"]
ddf_revdtc = ddf.read_csv('C:/Users/dvoruga/Desktop/PSGDTU/REVDTC.txt',sep='\\u0001',names=headers_revdtc,engine='python',blocksize=64000000)

headers_gdts130_revnpitm = ["REVNPITM_IN_ITEM","REVNPITM_IN_STORE","REVNPITM_IN_ADDDT"]
ddf_revnpitm = ddf.read_csv('C:/Users/dvoruga/Desktop/PSGDTU/part00_SG_GDTS130_REVNPITM.txt',sep='\\u0001',names=headers_gdts130_revnpitm, engine='python',blocksize=64000000)

headers_gdtu100_dtcitem =["OLDDTC_IN_ITEM",
"OLDDTC_IN_STORE",
"REV_DTC_NUM",
"REV_DTCE_NUM",
"REV_TOTPLNS",
"REV_CUR_FACE",
"REV_CUR_PRES",
"REV_CUR_FILL",
"REV_CUR_CAP",
"REV_CHKOUT",
"REV_REC_CRDTE",
"REV_REC_LUDTE",
"REV_PLNBUS	",
"REV_CUR_DISP_FACE"]

# ddf_dtcitem = ddf.read_csv('C:/Users/dvoruga/Desktop/PSGDTU/part88_SG_GDTU100_DTCITEM.txt',sep='\\u0001',names=headers_revdtc,engine='python',blocksize=64000000)

rjoin = ddf.merge(ddf_revdtc, ddf_revnpitm, left_on= 'REV_ITEM',right_on= 'REVNPITM_IN_ITEM', how='right')

print(rjoin.head())

Gen_present = ddf_revdtc[['REV_ITEM',
'REV_STORE',
'REV_DTC_NUM',
'REV_DTCE_NUM',
'REV_TOTPLNS',
'REV_CUR_FACE',
'REV_CUR_PRES',
'REV_CUR_FILL',
'REV_CUR_CAP',
'REV_CHKOUT',
'REV_REC_CRDTE',
'REV_REC_LUDTE',
'REV_PLNBUS',
'REV_CUR_DISP_FACE']]

print(Gen_present)
print(time.process_time_ns())
print(time.process_time_ns()-t1)

# print(dff.head())
# print(type())
# print(df.npartitions)
# print(df.dtypes)
# df_compute = df.isnull().sum().compute()
# print(df_compute)
# df_groupby = df.groupby(['REVNPITM_IN_ADDDT'])
# print(df_groupby)
# print(df.shape())

# client = Client(processes=False, threads_per_worker=2, n_workers=3, memory_limit ='4GB')
# print(client)