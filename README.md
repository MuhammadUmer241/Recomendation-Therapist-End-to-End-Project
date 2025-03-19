

# Recomendation-system-End-to-End-Project

An end-to-end therapist recommendation system built with Django APIs, Chroma vector database, zero-shot learning for categorization, and data analytics. This project processes therapist data, generates recommendations, and provides insights through exploratory analysis.

## Project Structure
```
muhammadumer241-recomendation-system-end-to-end-project/
├── README.md              # Project documentation
├── LICENSE                # MIT License file
├── main.py                # Main script (if applicable)
├── manage.py              # Django management script
├── apis/                  # Django app for APIs
│   ├── models.py          # Database models
│   ├── serializer.py      # API serializers
│   ├── urls.py            # API endpoints
│   ├── views.py           # API logic
│   └── migrations/        # Database migrations
├── data/                  # Datasets and analytics results
│   ├── preprocessed_with_combine_text.csv  # Preprocessed data
│   ├── therapist data.csv                  # Raw therapist data
│   └── unique_records/    # Unique values extracted from data
│       ├── age_unique_records
│       ├── expertise_unique_records
│       ├── speciality_unique_records
│       └── therapy_ways_unique_records
├── mainproject/           # Django project settings
│   ├── settings.py        # Configuration
│   ├── urls.py            # Root URL routing
│   ├── asgi.py            # ASGI config
│   └── wsgi.py            # WSGI config
├── src/                   # Source code for analysis and processing
│   ├── analysis/          # Data analytics
│   │   └── data_analysis.ipynb  # Jupyter notebook for EDA
│   ├── make_index/        # Vector index creation
│   │   └── create_index.py      # Script to build Chroma index
│   └── ner/               # Named Entity Recognition and zero-shot logic
│       ├── unique_list.py # Extract unique entities
│       └── zero_short.py  # Zero-shot categorization
└── vectordb/              # Chroma vector database
    ├── chroma.sqlite3     # Database file
    └── cd5cbc64-.../      # Vector index files
```

## Features
1. **Django APIs**: RESTful endpoints (`apis/`) to serve therapist recommendations.
2. **Chroma Vector DB**: Stores vectorized therapist data for efficient similarity searches (`vectordb/`).
3. **Zero-Shot Learning**: Categorizes therapist attributes using zero-shot techniques (`src/ner/zero_short.py`).
4. **Data Analytics**: Exploratory analysis and visualizations in `src/analysis/data_analysis.ipynb`, with results in `data/`.

## Prerequisites
- Python 3.8+
- Django 4.x
- ChromaDB (`pip install chromadb`)
- Jupyter Notebook (`pip install notebook`)
- Other dependencies: `pip install -r requirements.txt` (create if not present)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MuhammadUmer241/Recomendation-Therapist-End-to-End-Project.git
   cd muhammadumer241-recomendation-therapist-end-to-end-project
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply Django migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

## Usage
- **APIs**: Access endpoints like `/api/` (defined in `apis/urls.py`) for recommendations.
- **Vector Index**: Run `src/make_index/create_index.py` to build or update the Chroma index.
- **Analytics**: Open `src/analysis/data_analysis.ipynb` in Jupyter to explore data insights.
- **Data**: Preprocessed data and unique records are in `data/`.

## How It Works
1. **Data Preprocessing**: Raw data (`therapist data.csv`) is cleaned and processed into `preprocessed_with_combine_text.csv`.
2. **Vectorization**: Therapist features are indexed in Chroma (`vectordb/`) via `create_index.py`.
3. **Zero-Shot Categorization**: `zero_short.py` infers categories without labeled data.
4. **Recommendations**: APIs match user queries to therapist vectors and return results.

## Future Improvements
- Add authentication to APIs.
- Enhance zero-shot model accuracy.
- Expand dataset for broader coverage.

## Contributing
Fork the repo, submit issues, or create pull requests to contribute!

## License
MIT License (see `LICENSE`).

---
