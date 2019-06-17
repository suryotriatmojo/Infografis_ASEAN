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

plt.figure('Bar Chart - Pendapatan Bruto Nasional Negara ASEAN', figsize = (12,8))
plt.bar(asean['Name'], asean['GNP'], color = colors)
plt.title('Pendapatan Bruto Nasional Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')

for j in range(len(asean)):
    plt.text(asean['Name'][j], asean['GNP'][j] + 1000, asean['GNP'][j])

plt.show()