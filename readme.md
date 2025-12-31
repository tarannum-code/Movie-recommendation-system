🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Machine Learning, and Streamlit.
The application recommends similar movies based on user selection and displays movie posters using the TMDB API.

🔗 Live Demo:
👉 https://movie-recommendation-system-92mn.onrender.com

🚀 Features

🔍 Select a movie from a dropdown

🎯 Get top 5 similar movie recommendations

🖼️ Displays movie posters using TMDB API

⚡ Fast and interactive Streamlit UI

☁️ Deployed live on Render

🧠 How It Works

Uses cosine similarity on movie feature vectors

Precomputed similarity matrix for fast recommendations

TMDB API is used to fetch movie posters dynamically

🛠️ Tech Stack

Python 3.11.9

Streamlit

Pandas

NumPy

Scikit-learn

TMDB API

Render (Deployment)

📂 Project Structure
movie-recommendation-system/
│
├── app.py               # Streamlit application
├── movies.pkl           # Movie metadata
├── similarity.pkl       # Similarity matrix (Git LFS)
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version (3.11.9)
├── README.md            # Project documentation

⚙️ Installation & Setup (Local)
1️⃣ Clone the repository
git clone https://github.com/tarannum-code/Movie-recommendation-system.git
cd Movie-recommendation-system

2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variable (TMDB API)

Create a .env file:

TMDB_API_KEY=your_tmdb_api_key_here

5️⃣ Run the app
streamlit run app.py

🌐 Live Deployment

The application is deployed on Render and accessible here:

👉 https://movie-recommendation-system-92mn.onrender.com

🔐 Security Note

TMDB API key is stored using environment variables

API keys are not hardcoded in the source code

Large files are managed using Git LFS

📌 Future Improvements

Add genre-based filtering

Show movie ratings & overview

Improve UI with cards and animations

Add collaborative filtering

Optimize similarity computation

👩‍💻 Author

Tarannum
GitHub: https://github.com/tarannum-code

⭐ Acknowledgements

TMDB for movie data & posters

Streamlit for rapid UI development
