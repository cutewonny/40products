import pandas as pd
df = pd.DataFrame(
    [["hong", "1990.01.02", "2021-0001"],
     ["김민준",	"1990.05.06", "2021-0002"],
     ["김철수", "2000.08.08","2021-0003"]
    ])
    
print(df)
df.to_excel(r'/Users/devwonny/Documents/40products/12. 엑셀의 정보를 불러와 수료증 자동 생성/엑셀생성.xlsx', index=False, header=False)