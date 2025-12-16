import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# --- SIDKONFIGURATION ---
st.set_page_config(page_title="Swing Radar", page_icon="📈", layout="wide")

# Mörkt tema för grafer
plt.style.use('dark_background')
plt.rcParams.update({"figure.facecolor": "black", "axes.facecolor": "black", "savefig.facecolor": "black"})

# --- S&P 500 LISTA (Förkortad för demo - lägg in hela din lista här) ---
UNIVERSE_TICKERS = [ 
"NVO",
"SNDK",
"MMM",
"AOS",
"ABT",
"ABBV",
"ACN",
"ADBE",
"AMD",
"AES",
"AFL",
"A",
"APD",
"ABNB",
"AKAM",
"ALB",
"ARE",
"ALGN",
"ALLE",
"LNT",
"ALL",
"GOOGL",
"MO",
"AMZN",
"AMCR",
"AEE",
"AEP",
"AXP",
"AIG",
"AMT",
"AWK",
"AMP",
"AME",
"AMGN",
"APH",
"ADI",
"AON",
"APA",
"APO",
"AAPL",
"AMAT",
"APTV",
"ACGL",
"ADM",
"ANET",
"AJG",
"AIZ",
"T",
"ATO",
"ADSK",
"ADP",
"AZO",
"AVB",
"AVY",
"AXON",
"BKR",
"BALL",
"BAC",
"BK",
"BAX",
"BDX",
"BRK-B",
"BBY",
"BIIB",
"TECH",
"BLK",
"BX",
"XYZ",
"BKNG",
"BXP",
"BSX",
"BMY",
"AVGO",
"BR",
"BRO",
"BF-B",
"BLDR",
"BG",
"CHRW",
"CDNS",
"CZR",
"CPT",
"CPB",
"COF",
"CAH",
"KMX",
"CCL",
"CARR",
"CAT",
"CBOE",
"CBRE",
"CDW",
"COR",
"CNC",
"CNP",
"CF",
"CRL",
"SCHW",
"CHTR",
"CVX",
"CMG",
"CB",
"CHD",
"CINF",
"CTAS",
"CSCO",
"C",
"CFG",
"CME",
"CMS",
"CTSH",
"COIN",
"CL",
"CMCSA",
"CAG",
"COP",
"ED",
"STZ",
"CEG",
"CPRT",
"GLW",
"CPAY",
"CTVA",
"CSGP",
"COST",
"CTRA",
"CRWD",
"CCI",
"CSX",
"CMI",
"CVS",
"DHI",
"DHR",
"DRI",
"DDOG",
"DVA",
"DAY",
"DECK",
"DE",
"DELL",
"DAL",
"DVN",
"DXCM",
"FANG",
"DLR",
"DG",
"DLTR",
"D",
"DPZ",
"DASH",
"DOV",
"DOW",
"DTE",
"DUK",
"DD",
"EMN",
"ETN",
"EBAY",
"ECL",
"EIX",
"EW",
"EA",
"ELV",
"LLY",
"EMR",
"ENPH",
"ETR",
"EOG",
"EPAM",
"EQT",
"EFX",
"EQIX",
"EQR",
"ERIE",
"ESS",
"EL",
"EG",
"EVRG",
"ES",
"EXC",
"EXE",
"EXPE",
"EXPD",
"EXR",
"XOM",
"FFIV",
"FDS",
"FICO",
"FAST",
"FRT",
"FDX",
"FIS",
"FITB",
"FSLR",
"FE",
"FI",
"F",
"FTNT",
"FTV",
"FOX",
"BEN",
"FCX",
"GRMN",
"IT",
"GE",
"GEHC",
"GEV",
"GEN",
"GNRC",
"GD",
"GIS",
"GM",
"GPC",
"GILD",
"GPN",
"GL",
"GDDY",
"GS",
"HAL",
"HAS",
"HCA",
"DOC",
"HSIC",
"HPE",
"HLT",
"HOLX",
"HD",
"HON",
"HRL",
"HST",
"HWM",
"HPQ",
"HUBB",
"HUM",
"HBAN",
"HII",
"IEX",
"IDXX",
"ITW",
"INCY",
"IR",
"PODD",
"INTC",
"ICE",
"IBM",
"IFF",
"IP",
"INTU",
"ISRG",
"IVZ",
"INVH",
"IQV",
"IRM",
"JBHT",
"JBL",
"JKHY",
"J",
"JNJ",
"JCI",
"JPM",
"K",
"KVUE",
"KDP",
"KEY",
"KEYS",
"KMB",
"KIM",
"KMI",
"KKR",
"KLAC",
"KR",
"LHX",
"LH",
"LRCX",
"LW",
"LVS",
"LDOS",
"LEN",
"LII",
"LIN",
"LYV",
"LKQ",
"LMT",
"L",
"LOW",
"LULU",
"LYB",
"MTB",
"MPC",
"MKTX",
"MAR",
"MMC",
"MLM",
"MAS",
"MA",
"MTCH",
"MKC",
"MCD",
"MCK",
"MDT",
"MRK",
"META",
"MET",
"MTD",
"MGM",
"MCHP",
"MU",
"MSFT",
"MAA",
"MRNA",
"MHK",
"MOH",
"TAP",
"MDLZ",
"MPWR",
"MNST",
"MCO",
"MS",
"MOS",
"MSI",
"MSCI",
"NDAQ",
"NTAP",
"NFLX",
"NEM",
"NWSA",
"NWS",
"NEE",
"NKE",
"NI",
"NDSN",
"NSC",
"NTRS",
"NOC",
"NCLH",
"NRG",
"NUE",
"NVDA",
"NVR",
"NXPI",
"OXY",
"ODFL",
"OMC",
"ON",
"OKE",
"ORCL",
"ORLY",
"OTIS",
"PCAR",
"PKG",
"PLTR",
"PANW",
"PSKY",
"PH",
"PAYX",
"PAYC",
"PYPL",
"PNR",
"PEP",
"PFE",
"PCG",
"PM",
"PSX",
"PNW",
"POOL",
"PPG",
"PPL",
"PFG",
"PG",
"PGR",
"PLD",
"PRU",
"PTC",
"PEG",
"PSA",
"PHM",
"QCOM",
"PWR",
"DGX",
"RL",
"RJF",
"O",
"REG",
"REGN",
"RF",
"RSG",
"RMD",
"RVTY",
"ROK",
"ROL",
"ROP",
"ROST",
"RCL",
"RTX",
"SPGI",
"CRM",
"SBAC",
"SLB",
"STX",
"SRE",
"NOW",
"SPG",
"SWKS",
"SW",
"SNA",
"SOLV",
"SO",
"LUV",
"SWK",
"SBUX",
"STT",
"STLD",
"STE",
"SYK",
"SMCI",
"SYF",
"SNPS",
"SYY",
"TROW",
"TTWO",
"TPR",
"TRGP",
"TGT",
"TEL",
"TDY",
"TER",
"TSLA",
"TXN",
"TXT",
"BA",
"CI",
"CLX",
"KO",
"COO",
"HIG",
"HSY",
"SJM",
"KHC",
"PNC",
"SHW",
"TTD",
"DIS",
"WMB",
"TMO",
"TJX",
"TKO",
"TMUS",
"TSCO",
"TT",
"TDG",
"TRV",
"TRMB",
"TFC",
"TYL",
"TSN",
"USB",
"UBER",
"UDR",
"ULTA",
"UNP",
"UAL",
"UPS",
"URI",
"UNH",
"UHS",
"VLO",
"V",
"VTR",
"VLTO",
"VRSN",
"VRSK",
"VZ",
"VRTX",
"VTRS",
"VICI",
"VST",
"VMC",
"WRB",
"GWW",
"WAB",
"WMT",
"WBD",
"WM",
"WAT",
"WEC",
"WFC",
"WELL",
"WST",
"WDC",
"WY",
"WSM",
"WTW",
"WDAY",
"WYNN",
"XEL",
"XYL",
"YUM",
"ZBRA",
"ZBH",
"ZTS"
]

# --- UI: TITEL & SIDEBAR ---
st.title("🚀 Swing Trading Radar")
st.markdown("Automatiserad analys av **Momentum (ROC)** och **Mean Reversion (RSI)**.")

with st.sidebar:
    st.header("⚙️ Inställningar")
    market_choice = st.radio("Marknad", ["USA (S&P 500)", "Sverige (Ladda upp fil)"])
    
    risk_kapital = st.number_input("Totalt Kapital (SEK)", value=200000, step=10000)
    risk_procent = st.slider("Risk per affär (%)", 0.5, 5.0, 1.0) / 100
    
    st.divider()
    
    rsi_limit = st.slider("Max RSI(5) för köp", 10, 50, 30)
    roc_period = st.number_input("ROC Period (Dagar)", value=146)
    
    run_btn = st.button("Kör Analys", type="primary")

# --- FUNKTIONER ---
def calc_rsi(series, period):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

@st.cache_data(ttl=3600) # Sparar data i cache i 1 timme
def get_data(tickers):
    return yf.download(tickers, period="2y", group_by='ticker', auto_adjust=True, progress=False)

# --- HUVUDLOGIK ---
if run_btn:
    tickers_to_scan = []
    market_index = "^GSPC" # Default US
    
    if market_choice == "USA (S&P 500)":
        tickers_to_scan = UNIVERSE_TICKERS
    else:
        st.info("För Sverige-analys, ladda upp Excel/CSV-filen här (Funktionalitet kan läggas till). Kör USA-demo så länge.")
        tickers_to_scan = UNIVERSE_TICKERS # Fallback för demo

    with st.status("Hämtar marknadsdata...", expanded=True) as status:
        # 1. HÄMTA DATA
        all_tickers = [market_index] + tickers_to_scan
        data = get_data(all_tickers)
        status.write("Data hämtad! Analyserar trender...")
        
        # 2. MARKNADSKOLL
        market_df = data[market_index] if len(all_tickers) > 1 else data
        market_curr = market_df['Close'].iloc[-1]
        market_sma200 = market_df['Close'].rolling(200).mean().iloc[-1]
        
        bull_market = market_curr > market_sma200
        
        # Visa Marknadsstatus högst upp
        col1, col2, col3 = st.columns(3)
        col1.metric("S&P 500 Pris", f"{market_curr:.0f}")
        col2.metric("SMA 200 Golv", f"{market_sma200:.0f}")
        
        if bull_market:
            col3.success("🟢 BULL MARKET (Köp Dippar)")
        else:
            col3.error("🔴 BEAR MARKET (Var försiktig)")
            
        # 3. SCANNA AKTIER
        candidates = []
        progress_bar = st.progress(0)
        
        for i, ticker in enumerate(tickers_to_scan):
            try:
                # Uppdatera progress bar
                progress_bar.progress((i + 1) / len(tickers_to_scan))
                
                df = data[ticker].copy() if len(all_tickers) > 1 else pd.DataFrame()
                if df.empty or len(df) < 200: continue
                
                close = df['Close']
                curr = close.iloc[-1]
                sma200 = close.rolling(200).mean().iloc[-1]
                
                # Trendfilter
                if curr < sma200: continue
                
                # Indikatorer
                rsi = calc_rsi(close, 5).iloc[-1]
                # FIX: fill_method=None för att slippa varningen
                roc = close.pct_change(periods=roc_period, fill_method=None).iloc[-1] * 100
                
                if rsi < rsi_limit and roc > 0:
                    # Riskhantering
                    stop_loss = sma200 * 0.98
                    risk_per_share = curr - stop_loss
                    shares = int((risk_kapital * risk_procent) / (risk_per_share * 10.5)) # Valuta ca 10.5
                    
                    candidates.append({
                        'Ticker': ticker,
                        'Pris': curr,
                        'RSI(5)': rsi,
                        'ROC(146)': roc,
                        'SMA200': sma200,
                        'Stop Loss': stop_loss,
                        'Antal': shares
                    })
            except Exception: continue
            
        status.update(label="Analys klar!", state="complete", expanded=False)

    # --- RESULTAT ---
    if candidates:
        df_res = pd.DataFrame(candidates).sort_values(by='ROC(146)', ascending=False)
        
        st.subheader(f"🎯 Hittade {len(candidates)} Köpkandidater")
        st.caption("Sorterat på Momentum (Högst ROC först)")
        
        # Visa interaktiv tabell
        st.dataframe(
            df_res[['Ticker', 'Pris', 'RSI(5)', 'ROC(146)', 'Stop Loss', 'Antal']].style.format({
                "Pris": "{:.2f}", 
                "RSI(5)": "{:.1f}", 
                "ROC(146)": "{:.1f}%",
                "Stop Loss": "{:.2f}"
            }),
            use_container_width=True
        )
        
        # --- GRAFER (TOP 12) ---
        st.subheader("📈 Grafer (Top 12)")
        
        top_picks = df_res.head(12)
        cols = st.columns(3) # 3 grafer i bredd
        
        for index, row in top_picks.iterrows():
            ticker = row['Ticker']
            col_idx = list(top_picks.index).index(index) % 3
            
            with cols[col_idx]:
                hist = data[ticker]['Close'].tail(roc_period)
                rsi_hist = calc_rsi(hist, 5)
                
                fig, ax = plt.subplots(figsize=(5, 3))
                ax.plot(hist.index, hist.values, color='#00FFFF', lw=1.5) # Cyan
                ax.set_title(f"{ticker} | RSI: {row['RSI(5)']:.1f}", color='white', fontsize=10)
                ax.axis('off') # Tar bort axlar för renare look
                
                # Lägg till RSI som liten "minigraf" under eller i samma
                # För enkelhetens skull, bara pris här
                
                st.pyplot(fig)
                
                with st.expander(f"Detaljer {ticker}"):
                    st.write(f"**Target:** {row['Pris']*1.1:.2f}")
                    st.write(f"**Stop:** {row['Stop Loss']:.2f}")

    else:
        st.warning("Inga aktier matchade dina kriterier just nu.")
