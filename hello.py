import streamlit as st
import pandas as pd

st.title("🌮Taco-kalkulator")

st.write("Beregn hvor mye du trenger til fredagstacoen basert på antall personer.")

# Velg antall personer
antall_personer = st.slider("Velg antall personer", 1, 20, 4)

# Enkle beregninger per person (du kan justere tallene som du vil)
ingredienser = {
    "Kjøttdeig (g)": 180,
    "Tacolefser (stk)": 2,
    "Revet ost (g)": 100,
    "Salat (g)": 50,
    "Tomat (g)": 50,
    "Agurk (g)": 50,
    "Mais (g)": 50,
    "Paprika (g)": 50,
    "Løk (g)": 50,
    "Rømme (bok)": 1/3,
    "Salsa (glass)": 1/3,
    "Avocado (stk)": 1,
}

# Kalkuler totaler
beregnet = {ing: mengde * antall_personer for ing, mengde in ingredienser.items()}

# Vis resultatet i tabell
df = pd.DataFrame.from_dict(beregnet, orient="index", columns=["Mengde totalt"])
st.subheader("Handleliste")
st.write(df)
st.write("Pris per pers på fellesen: ca 10 kr. ")
