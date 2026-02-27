

🌸 Cora: AI-Powered PCOS Diagnostic Suite

**Cora** is a high-performance medical assistant designed to bridge the gap between complex hormonal data and patient-friendly insights. Built for 2026, it leverages **XGBoost** for clinical-grade risk assessment and **llama-3.1-8b** for personalized medical recommendations.

🚀 Features

* **Advanced Risk Prediction**: Uses an **XGBoost Classifier** to analyze five key biomarkers (Age, BMI, Menstrual Cycle, Testosterone, and Follicle Count).
* **AI Medical Consultant**: Integrated **GROQ AI (Cora)** provides context-aware lifestyle and medication guidance based on diagnostic results.
* **Interactive Analytics**: A "Neon-Themed" dashboard built with **Seaborn** and **Matplotlib** to visualize patient metrics against clinical thresholds.
* **Dynamic Reporting**: Instant PDF and CSV generation for patients to share data with their healthcare providers.

🛠️ Technical Stack

**Frontend**: [Streamlit](https://streamlit.io/) (Python-based Web Framework)
**Machine Learning Brain**: [XGBoost](https://xgboost.readthedocs.io/) (Extreme Gradient Boosting) **Large Language Model**: [GROQ AI API]
**Data Processing**: Pandas, NumPy
**Visualization**: Seaborn, Matplotlib
**Report Generation**: FPDF

📂 File Structure

```text
├── .streamlit/           # Streamlit configuration
├── images/               # Knowledge Centre assets
├── diagnosis.py          # Main UI: Diagnosis & AI Chatbot
├── kc.py                 # Knowledge Centre: Information portal
├── result.py             # Analytics Dashboard: Seaborn visualizations
├── web_functions.py      # Core logic: XGBoost training and prediction
├── PCOS.csv              # Training dataset
└── requirements.txt      # List of dependencies

```

⚙️ Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/pcos-ai-system.git
cd pcos-ai-system

```


2. **Install Dependencies**:
```bash
pip install -r requirements.txt

```


3. **Set up your API Key**:
Create a `.env` file or add your key to Streamlit secrets:
```text
GEMINI_API_KEY = "your_google_gemini_api_key_here"

```


4. **Run the Application**:
```bash
streamlit run main.py

```



 🧠 The AI Logic

### The "Math Brain" (XGBoost)

The system uses a boosted decision tree architecture. Unlike a single Decision Tree, XGBoost builds trees sequentially, with each new tree correcting the errors of the previous ones.

### The "Language Brain" (Groq)

The prediction probability (e.g., 85% risk) is passed to Groq as context. This ensures that the advice provided is not generic, but specifically tailored to the severity of the biomarkers detected.

---

### ⚠️ Disclaimer

*This tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a physician.*

