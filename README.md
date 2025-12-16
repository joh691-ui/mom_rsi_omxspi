#🚀 Swing Radar**Swing Radar** är en interaktiv trading-dashboard byggd med Python och Streamlit. Den scannar automatiskt av marknaden (S&P 500) för att hitta aktier med starkt momentum som befinner sig i en tillfällig rekyl ("Buy the Dip").

Verktyget visualiserar marknadsläget, filtrerar fram de bästa kandidaterna och beräknar positionsstorlekar baserat på din riskprofil.

##📊 Funktioner* **Marknadskoll:** Analyserar automatiskt om S&P 500 ligger över/under MA200 för att avgöra om det är Bull eller Bear market.
* **Automatisk Scanning:** Går igenom hundratals aktier på några sekunder.
* **Riskhantering:** Beräknar antal aktier att köpa baserat på ditt konto och vald riskprocent.
* **Dark Mode UI:** Snyggt och lättläst gränssnitt optimerat för trading.
* **Interaktiva Grafer:** Visar prishistorik och RSI-nivåer för de bästa kandidaterna.

##🧠 StrateginScriptet bygger på en klassisk **Momentum + Mean Reversion** strategi:

1. **Trendfilter:** Aktien måste handlas *över* sitt 200-dagars glidande medelvärde (SMA200). Vi handlar bara i upptrender.
2. **Momentum:** Aktien måste ha en positiv Rate of Change (ROC) över en längre period (standard 146 dagar). Vi vill ha starka aktier.
3. **Rekyl (Entry):** RSI(5) ska vara under ett gränsvärde (standard 30). Detta indikerar att aktien är tillfälligt översåld och erbjuder ett bra köpläge.

##🛠 InstallationFör att köra detta lokalt på din dator behöver du ha Python installerat.

1. **Klona repot (eller ladda ner filerna):**
```bash
git clone https://github.com/ditt-anvandarnamn/swing-radar.git
cd swing-radar

```


2. **Installera beroenden:**
Skapa gärna en virtuell miljö först. Kör sedan:
```bash
pip install -r requirements.txt

```


*(Om du inte har en requirements-fil, se nedan vad som behövs)*
3. **Starta applikationen:**
```bash
streamlit run app.py

```



##📦 Beroenden (Requirements)Om du skapar en `requirements.txt`, klistra in detta innehåll:

```text
streamlit
yfinance
pandas
matplotlib

```

##⚙️ AnvändningNär du startat appen öppnas den i din webbläsare. I sidomenyn till vänster kan du justera:

* **Totalt Kapital:** Ditt kontovärde i SEK.
* **Risk per affär:** Hur stor % av kapitalet du vill riskera per trade (avgör positionsstorleken).
* **RSI Gräns:** Hur djupt översåld aktien måste vara (t.ex. under 30).
* **ROC Period:** Tidsperiod för att mäta momentum.

Tryck på **"Kör Analys"** för att hämta data och se resultatet.

##⚠️ DisclaimerDetta verktyg är endast avsett för utbildningssyfte och analys. All handel med värdepapper innebär en risk för kapitalförlust. Historisk avkastning är ingen garanti för framtida resultat. Användaren ansvarar själv för alla investeringsbeslut.

---

##📝 Att göra (Tips för utveckling)* [ ] Lägga till funktion för att ladda upp egen CSV-fil med svenska aktier.
* [ ] Lägga till stöd för e-postnotiser vid träffar.
* [ ] Utöka S&P 500-listan till att inkludera alla 500 bolag (listan i koden är förkortad).

---

*Skapad med ❤️ och Python.*
