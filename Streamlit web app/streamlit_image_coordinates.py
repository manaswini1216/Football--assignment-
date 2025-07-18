import streamlit as st
import streamlit.components.v1 as components
import json

def streamlit_image_coordinates(image, key="pil"):
    canvas_key = f"{key}_canvas"
    image_placeholder = st.empty()
    image_placeholder.image(image)

    clicked_coords = st.session_state.get(canvas_key, None)

    components.html(
        f"""
        <script>
        const image = window.parent.document.querySelector('img[alt="{canvas_key}"]');
        if (image) {{
            image.style.cursor = 'crosshair';
            image.onclick = function(e) {{
                const rect = image.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const coords = {{"x": Math.round(x), "y": Math.round(y)}};
                window.parent.postMessage({{"type": "streamlit:setComponentValue", "key": "{canvas_key}", "value": JSON.stringify(coords)}}, "*");
            }};
        }}
        </script>
        """,
        height=0
    )

    if clicked_coords is not None:
        return json.loads(clicked_coords)
    else:
        return None
