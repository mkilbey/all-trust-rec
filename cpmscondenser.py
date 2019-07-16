import pandas as pd
df = pd.read_csv('All FY Recruitment Summary.csv', encoding = "ISO-8859-1", sep="|")
df['TrustName'].value_counts()
g_list = df[df['TrustName'] == "GUY'S AND ST THOMAS' NHS FOUNDATION TRUST"]
g_list.to_csv('gstt_cpms_all.csv')
