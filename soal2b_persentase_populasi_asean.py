import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'darkgrid')

mydb = sqlalchemy.create_engine(
    # DB_system ://user:pass@host:port/nama_database
    'mysql+pymysql://root:Bestfriend181091@localhost:3306/world'
)

query_country = 'select * from country'
df_country = pd.read_sql(query_country, mydb)

asean = df_country[df_country['Region'] == 'Southeast Asia'].reset_index()

plt.figure('Pie Chart - Populasi Negara ASEAN', figsize = (12,8))

plt.pie(asean['Population'], labels = asean['Name'], autopct='%1.1f%%', textprops={'color': 'black'})
plt.title('Persentase Penduduk ASEAN')
plt.legend(asean['Name'], bbox_to_anchor=(1, 1), loc = 0)

plt.show()