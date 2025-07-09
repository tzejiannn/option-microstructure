<body>
  <h1>AAPL Option Market Microstructure Analysis</h1>

  <h2>1. Project Overview</h2>
  <p>This project aims to conduct a cross-sectional analysis of an option across multiple expiry dates to study liquidity, bid-ask spreads, volume, open interest, and moneyness. The goal is to uncover structural patterns in option pricing and trading behavior on a highly liquid stock </p>
  
  <h2>Data Collection &amp; Analysis Scope</h2>
  <p>Data was collected from Yahoo Finance using Selenium to automate browser interaction and scrape option chain data for multiple expiry dates.
  <p>Scripts for data scraping and combining CSV files are provided in the <code>scripts</code> folder.</p>
  
  <p>This project collects AAPL options data for multiple expiry dates, all captured on <strong>July 8th, 2024</strong>, when the underlying stock closing price was approximately <strong>$210.01</strong>.</p>
  <p><strong>Note:</strong> Since the data snapshot is from a single trading day, the analysis focuses on the option market microstructure <em>as it existed on that day</em>. This means:</p>
  <ul>
    <li>Moneyness and pricing are calculated relative to the spot price on July 8th.</li>
    <li>Time-to-expiry and liquidity patterns reflect this fixed point in time.</li>
  </ul>

  <p>For a more dynamic or longitudinal analysis of option behavior over time, collecting data across multiple dates would be necessary. However, this project’s scope is a <em>cross-sectional</em> analysis of option market characteristics on a specific date.</p>


  <h2>3. Data Description</h2>
  <p>The dataset contains the following key fields:</p>
  <ul>
    <li><code>contract_name</code></li>
    <li><code>last_trade_date</code></li>
    <li><code>strike</code></li>
    <li><code>last_price</code></li>
    <li><code>bid</code></li>
    <li><code>ask</code></li>
    <li><code>change</code></li>
    <li><code>pct_change</code></li>
    <li><code>volume</code></li>
    <li><code>open_interest</code></li>
    <li><code>implied_volatility</code></li>
    <li><code>expiry</code></li>
  </ul>

  <h2>4. Analysis Plan</h2>
  <ul>
    <li>Calculate bid-ask spread and relative spread</li>
    <li>Categorize options by moneyness (ITM, ATM, OTM) based on spot price</li>
    <li>Analyze liquidity profiles via volume and open interest</li>
    <li>Examine spread behavior across strike, expiry, and option type (call/put)</li>
    <li>Visualize findings using seaborn and matplotlib</li>
  </ul>

  <h2>5. Usage</h2>
  <p>Run the Jupyter notebooks in the <code>notebooks</code> folder to reproduce data analysis and visualizations.<br />
  To update or extend data, use the Python scripts in <code>scripts</code> for scraping, cleaning and combining option data.</p>

  <h2>6. Results &amp; Visualizations</h2>
  <p>Includes boxplots of spreads by moneyness, heatmaps of volume by strike and expiry, and scatterplots analyzing liquidity measures.</p>

  <h2>7. Limitations &amp; Future Work</h2>
  <ul>
    <li>Data collected as a single-day snapshot limits longitudinal insights.</li>
    <li>Future versions will automate daily data collection for time-series analysis.</li>
    <li>Additional features like implied volatility surface modeling can be explored.</li>
  </ul>

  <h2>8. Dependencies</h2>
  <ul>
    <li>Python 3.8+</li>
    <li>pandas</li>
    <li>numpy</li>
    <li>matplotlib</li>
    <li>seaborn</li>
    <li>yahoo_fin</li>
  </ul>
  <p>See <code>requirements.txt</code> for exact versions.</p>

  <h2>9. Folder Structure</h2>
  <pre>
option-microstructure/
├── data/                   # Raw and processed data files (CSV)
├── notebooks/              # Jupyter notebooks for EDA and visualization
├── scripts/                # Data scraping and processing scripts
├── combined/               # Combined datasets output folder
├── README.md
├── requirements.txt
  </pre>

  <h2>10. Contact</h2>
  <p>Joel Ang — <a href="mailto:joel.ang.tze.jian@u.nus.edu">joel.ang.tze.jian@u.nus.edu</a><br />
  LinkedIn: <a href="https://www.linkedin.com/in/tzejian/" target="_blank" rel="noopener noreferrer">https://www.linkedin.com/in/tzejian/</a></p>
</body>
</html>
