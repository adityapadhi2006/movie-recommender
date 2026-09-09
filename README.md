# 🎬 Content-Based Movie Recommender System

A full-stack machine learning web application that recommends similar movies based on plot descriptions, genres, cast, crew, and keywords using Cosine Similarity.

🔗 **Live Demo:** [movie-recommender-adityapadhi.streamlit.app](https://movie-recommender-adityapadhi.streamlit.app/)

---

## 📌 Architecture & Workflow
1. **Data Preprocessing:** Merged TMDB 5000 Movies & Credits datasets. Extracted genres, keywords, top 3 cast members, and the director using `ast.literal_eval`.
2. **Text Normalization:** Collapsed spaces to eliminate entity ambiguity, stemmed words with NLTK's `PorterStemmer`, and generated a unified `tags` feature.
3. **Vectorization:** Transformed tags into a 5,000-dimensional coordinate space using `CountVectorizer` (Bag-of-Words) with stop-word removal.
4. **Similarity Engine:** Calculated pairwise angular distances using **Cosine Similarity**.
5. **Dynamic Poster API:** Connected to TMDB REST API to fetch high-resolution posters on demand.
6. **Deployment:** Hosted on Streamlit Community Cloud with secure credential management via `st.secrets`.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & ML:** Pandas, NumPy, Scikit-learn, NLTK
* **Web UI & Deployment:** Streamlit, Streamlit Community Cloud
* **External APIs:** The Movie Database (TMDB) API

---

## 💻 Local Setup

```bash
# Clone the repository
git clone [https://github.com/adityapadhi2006/movie-recommender.git](https://github.com/adityapadhi2006/movie-recommender.git)
cd movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
