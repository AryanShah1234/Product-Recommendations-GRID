import pickle
import streamlit as st
import pandas as pd
import time

product_dict=pickle.load(open('data_dict1.pkl','rb'))
products_cleaned_df=pd.DataFrame(product_dict)
sig=pickle.load(open('sig.pkl','rb'))
indices=pickle.load(open('indices.pkl','rb'))

st.set_page_config(
    page_title="VITA-FUSION",
    page_icon="🧊",
    layout="wide",
    
)

def give_rec_spec(product_name, sig=sig):
    # Get the index corresponding to unique Id
    uniqueId = products_cleaned_df.loc[products_cleaned_df['product_name']==product_name,'uniq_id'].values[0]
    idx = indices[uniqueId]
    # Get the pairwsie similarity scores
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar products
    sig_scores = sig_scores[1:11]

    # Product indices
    product_indices = [i[0] for i in sig_scores]

    # Top 10 most similar products
    name=[]
    img=[]
    for i in range(0,10):
        name.append(products_cleaned_df.iloc[product_indices].product_name.values[i])
        img.append(products_cleaned_df.iloc[product_indices].image.values[i])
    return name,img


def helper(product):
    return product[2:-2].split('", "')

st.title('Flipkart')
st.divider()
selected_product =st.selectbox('Search Product',products_cleaned_df['product_name'].values)
if st.button('Recommend'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
    name_list,img_list= give_rec_spec(selected_product)
    prod_img=[]
    for i in range(0,10):
        prod_img.append(helper(img_list[i])[0])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(prod_img[0],caption=name_list[0])
        st.image(prod_img[3],caption=name_list[3])
        st.image(prod_img[6],caption=name_list[6])
    with col2:
        st.image(prod_img[1],caption=name_list[1])
        st.image(prod_img[4],caption=name_list[4])
        st.image(prod_img[7],caption=name_list[7])

    with col3:
        st.image(prod_img[2],caption=name_list[2])
        st.image(prod_img[5],caption=name_list[5])
        st.image(prod_img[8],caption=name_list[8])