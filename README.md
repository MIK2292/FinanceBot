# FinanceBot
Questo è il progetto che ci porterà a non morire di fame un giorno (oppure a chiedere l'elemosina).

Per ora si compone semplicemente di un main e del file myfinance.py, quest'ultimo crea i metodi che verranno usati nel main.

Per ora tutto quello che fa è testare un modello molto basico di bot su dei dati storici, viene semplicemente riportato il saldo finale e lo storico dei movimenti. 

# Installazione e run in locale 
serve la libreria yfinance di python (https://pypi.org/project/yfinance/)
si può utilizzare 
```bash
pip install  --upgrade --no-cache-dir
```
per la sua installazione


# Prossimi passi 
Vorrei aggiungere un modo automatico per valutare le performance del bot, cioè voglio che a partire da un algoritmo di compravendita e dai dati storici di un asset abbiamo un report completo di grafici, analisi statistiche e tutto ciò che serve er valutare la performance del bot.
