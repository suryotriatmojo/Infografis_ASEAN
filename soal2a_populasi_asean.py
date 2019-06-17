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

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'gray', 'yellow', 'pink', 'black', 'darkblue']

plt.figure('Bar Chart - Populasi Negara ASEAN', figsize = (12,8))
plt.bar(asean['Name'], asean['Population'], color = colors)
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa')

for j in range(len(asean)):
    plt.text(asean['Name'][j], asean['Population'][j] + 1000000, asean['Population'][j])

plt.show()