import pandas as pd

# Завантажуємо датафрейм 
df = pd.read_csv('GoogleApps.csv')
print(df)
df.info
# Як називається програма, розташована першим у наборі даних?
print(df.describe())

# До якої категорії відноситься додаток, розташований останнім у наборі даних?


# Скільки стовпців міститься у наборі даних?
# Дані якого типу зберігаються у кожному зі стовпців?


# Вкажіть середнє арифметичне та медіану розміру додатків (Size)
# Скільки коштує найдорожчий додаток?
# *Вкажіть середнє арифметичне та медіану кількості установок програм (Installs)
