import streamlit as st

from wine_core import FOOTER

st.set_page_config(page_title="Prediksi Kualitas Wine", page_icon="🍷", layout="wide")

halaman = {
    "Pengantar": [
        st.Page("beranda.py", title="Beranda", icon=":material/home:", default=True),
        st.Page("dataset.py", title="Dataset", ...),
        st.Page("eda.py", title="EDA", ...),
    ],
}
    ],
    "Pengolahan & Model": [
        st.Page("views/preprocessing.py", title="Preprocessing", icon=":material/tune:"),
        st.Page("views/pca.py", title="Reduksi Dimensi (PCA)", icon=":material/scatter_plot:"),
        st.Page("views/modelling.py", title="Modelling & Evaluasi", icon=":material/model_training:"),
    ],
    "Penerapan": [
        st.Page("views/prediksi_satu.py", title="Prediksi Satu Wine", icon=":material/wine_bar:"),
        st.Page("views/prediksi_massal.py", title="Prediksi Massal (CSV)", icon=":material/upload_file:"),
        st.Page("views/kesimpulan.py", title="Kesimpulan & Saran", icon=":material/task_alt:"),
    ],
}

pg = st.navigation(halaman)

with st.sidebar:
    st.divider()
    st.caption(FOOTER)

pg.run()
