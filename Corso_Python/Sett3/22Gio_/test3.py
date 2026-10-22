#manipolazione dati e intervalli temporali

import pandas as pd

'''
'D'	Every day
'W'	Every week (doesn't start on sunday)
'h'	Every hour
'MS'	Start of every month
'ME'/'M'	End of every month
'''
#generazione serie di date
#start = date of start, periods = number of dates, freq=frequency of dates
#funziona come una serie
dr = pd.date_range(start='2026-01-01', periods=5, freq='7D')
print(dr)
print(dr[4])

df = pd.DataFrame({
    'Sales': [100, 200, 150, 300, 250]
}, index=dr)

print("DF")
print(df)
#If a dataframe has dates as index, you can resample it by frequency.
#What this does is recreate the dataframe but with dates of different frequency.
dfrsm = df.resample('M').sum()
print("DFRS")
print(dfrsm)

'''dfrsd = df.resample('D').sum()
print("DFRS")
print(dfrsd)'''

#resample into days
dfrsd = df.resample('D').ffill()

#Create empty days for the last week.
# Alternatively, one last day through singular date.
emptydays = pd.DataFrame(
    #leave {Sales = []} empty
    index=pd.date_range(
        start= df.index[-1] + pd.Timedelta(days=1),
        periods=6,
        freq='D'
    )
)
#Add empty days to the resampled dataframe.
dfrsd = pd.concat([dfrsd, emptydays])

#fill empty values and divide all by 7 to split
dfrsd['Sales'] = dfrsd['Sales'].ffill() / 7

print("ED")
print(emptydays)

print("DFRSD")
print(dfrsd)

#serie dei giorni interpolati
gint = emptydays.iloc[0:].index
print("Giorni interpolati:\n", gint.strftime('%Y/%m/%d').tolist())
#.strftime() string from time. Gli elementi vengono convertiti in una lista con tolist
# oppure list(...)

#to_datetime converte una stringa in una variabile datetime
date = '02/02/2026'  # string
date = pd.to_datetime(date, format='%d/%m/%Y')
print("Data convertita")
print(date)
print("Date spostate di un periodo")
print(gint.shift(1))
print("Variazione giornaliera:")
print(dfrsd['Sales'].pct_change())

#finestra temporale scorrevole
# fa calcolo per ogni elemento e considera nel calcolo un numero window di elementi.
# window = elementi considerati.
# primo elemento non ha considerato nessuno elemento ancora tranne uno, quindi
# l'operazione non si svolge.
print(dfrsd['Sales'].rolling(window=2).mean())