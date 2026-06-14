
import streamlit as st
import pandas as pd
import os

# =========================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================

st.set_page_config(
    page_title="STREETWEAR WHITE",
    page_icon="🔥",
    layout="wide"
)

# =========================================
# ESTILOS CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"]{
    background-color:#0d0d0d;
    color:white;
    font-family:Arial;
}

/* TITULO */

.titulo{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    margin-top:20px;
    letter-spacing:4px;
}

/* ESLOGAN */

.eslogan{
    text-align:center;
    color:#9e9e9e;
    font-size:22px;
    margin-bottom:50px;
}

/* TARJETAS */

.product-card{
    background:#161616;
    border-radius:20px;
    padding:15px;
    border:1px solid #2c2c2c;
    margin-bottom:25px;
    transition:0.3s;
}

.product-card:hover{
    transform:scale(1.02);
    border:1px solid white;
}

/* IMAGENES */

.product-img img{
    width:100%;
    height:420px;
    object-fit:cover;
    border-radius:15px;
}

/* PRECIO */

.precio{
    color:#00ff88;
    font-size:24px;
    font-weight:bold;
    margin-top:10px;
    margin-bottom:15px;
}

/* BOTON */

.stButton > button{
    width:100%;
    height:45px;
    border:none;
    border-radius:12px;
    background:white;
    color:black;
    font-weight:bold;
    transition:0.3s;
}

.stButton > button:hover{
    background:#00ff88;
    color:black;
}

/* CONTACTO */

.contacto{
    background:#151515;
    padding:30px;
    border-radius:20px;
    border:1px solid #333;
    margin-top:50px;
}

/* FOOTER */

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITULO
# =========================================

st.markdown(
    '<div class="titulo">👖 STREETWEAR WHITE 👕</div>',
    unsafe_allow_html=True
)

# =========================================
# ESLOGAN
# =========================================

st.markdown(
    '<div class="eslogan">"Barato como la carne de gato"</div>',
    unsafe_allow_html=True
)

# =========================================
# PRODUCTOS
# =========================================

productos = [

    {
        "nombre":"Mangalarga Affliction - Talla L",
        "precio":"$300 MXN",
        "imagen":"aff.jpeg"
    },

    {
        "nombre":"Suéter Interstate - Talla M",
        "precio":"$350 MXN",
        "imagen":"inter.jpeg"
    },

    {
        "nombre":"Mangalarga Southpole - Talla L",
        "precio":"$400 MXN",
        "imagen":"mangalarga.jpeg"
    },

    {
        "nombre":"Camisa Ed Hardy - Talla M",
        "precio":"$300 MXN",
        "imagen":"edhardy.jpeg"
    },

    {
        "nombre":"Hoodie Disparame - Talla L",
        "precio":"$300 MXN",
        "imagen":"disparame.jpeg"
    },

    {
        "nombre":"Short JNCO Buddha - Talla 34",
        "precio":"$300 MXN",
        "imagen":"jnco.jpeg"
    },

    {
        "nombre":"Camisa Christian Audigier - Talla M",
        "precio":"$200 MXN",
        "imagen":"cristian.jpeg"
    },

    {
        "nombre":"Pantalón Southpole - Talla 36",
        "precio":"$600 MXN",
        "imagen":"pantalon.jpeg"
    },

    {
        "nombre":"Suéter Racing Fox - Talla L",
        "precio":"$300 MXN",
        "imagen":"fox.jpeg"
    },

    {
        "nombre":"Suéter JNCO Pantera - Talla L",
        "precio":"$450 MXN",
        "imagen":"panter.jpeg"
    },

    {
        "nombre":"Chamarra Southpole Bboy - Talla XL",
        "precio":"$500 MXN",
        "imagen":"boy.jpeg"
    }

]

# =========================================
# COLUMNAS
# =========================================

cols = st.columns(3)

# =========================================
# MOSTRAR PRODUCTOS
# =========================================

for i, producto in enumerate(productos):

    with cols[i % 3]:

        st.markdown(
            '<div class="product-card">',
            unsafe_allow_html=True
        )

        # =========================================
        # IMAGEN
        # =========================================

        try:

            st.image(
                producto["imagen"],
                use_container_width=True
            )

        except:

            st.warning(
                "Imagen no encontrada"
            )

        # =========================================
        # NOMBRE
        # =========================================

        st.subheader(
            producto["nombre"]
        )

        # =========================================
        # PRECIO
        # =========================================

        st.markdown(
            f'<div class="precio">{producto["precio"]}</div>',
            unsafe_allow_html=True
        )

        # =========================================
        # BOTÓN
        # =========================================

        if st.button(
            "🛒 Comprar",
            key=producto["nombre"]
        ):

            st.success(
                f"{producto['nombre']} agregado al carrito 🔥"
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

# =========================================
# CONTACTO
# =========================================

st.markdown("---")

st.markdown("""

<div class="contacto">

<h2>📞 CONTACTO</h2>

<p><b>WhatsApp:</b> +52 984 176 1750</p>

<p><b>Correo:</b> Streetwearwhitee@gmail.com</p>

<p><b>Ubicación:</b> Playa del Carmen, Quintana Roo</p>

</div>

""", unsafe_allow_html=True)

# =========================================
# FOOTER
# =========================================

st.markdown(
    '<div class="footer">STREETWEAR WHITE © 2026</div>',
    unsafe_allow_html=True
)
