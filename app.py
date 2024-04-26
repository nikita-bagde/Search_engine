import streamlit as st
import chromadb


######################
st.balloons()
st.image("images/img.png")
st.title('🚀 📺 Enhancing Search Engine Relevance for Video Subtitles 🎦 ')
st.subheader('🔍 Navigating Multilingual Movie Moments 🍿')
######################


client = chromadb.PersistentClient(path="/Internship")
client.heartbeat()
collection = client.get_collection(name="Search_Engine")


query_text = st.text_input('Enter your query:')
if st.button('Search'):
    st.snow()
    def similar_title(query_text):
        result = collection.query(
            query_texts=[query_text],
            include=["metadatas", "distances"],
            n_results=10
        )
        ids = result['ids'][0]
        distances = result['distances'][0]
        metadatas = result['metadatas'][0]
        sorted_data = sorted(zip(metadatas, ids, distances), key=lambda x: x[2], reverse=True)
        return sorted_data

    result_data = similar_title(query_text)
    

    st.success('Here are the most relevant subtitle names :')
    for metadata, ids, distance in result_data:
        subtitle_name = metadata['name']
        subtitle_id = metadata['num']
        st.markdown(f"[{subtitle_name}]")