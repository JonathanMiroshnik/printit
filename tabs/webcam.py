from i18n import t
"""Webcam tab content."""

import streamlit as st
import os
from PIL import Image


def render(preper_image,printer_info, print_image):
    """Render the Webcam tab."""
    st.subheader(t("webcam_tab_title"))
    on = st.toggle(t("ask_camera_permission"))
    if on:
        picture = st.camera_input(t("take_a_picture"))
        if picture is not None:
            # Convert and process image
            picture = Image.open(picture).convert("RGB")
            grayscale_image, dithered_image = preper_image(picture, label_width=printer_info['label_width'])

            # Display processed image
            st.image(dithered_image, caption=t("dithered_image_cap"))

            # Print options
            colc, cold = st.columns(2)
            with colc:
                if st.button(t("print_rotated"), key="print_rotated_webcam"):
                    print_image(grayscale_image, printer_info, rotate=90, dither=True)
                    st.balloons()
                    st.success(t("image_sent_rotated"))
            with cold:
                if st.button(t("print_webcam"), key="print_webcam"):
                    print_image(grayscale_image, printer_info, dither=True)
                    st.success(t("image_sent"))
