from i18n import t
"""FAQ tab content."""

import streamlit as st
from PIL import Image


def render():
    """Render the FAQ tab."""
    st.subheader(t("faq_title"))
    st.markdown(
        """
        - *שיטוח (Dithering)* מומלץ (ולפעמים מחייב) אם המקור אינו קווי, כי גווני אפור וצבע נראים רע במדפסת תרמית
        - מעבר בין לשוניות לא מאתר מחדש מדפסות, רענון העמוד יאלץ זיהוי מחדש
        - כדי לשמור את התמונות המופקות על השרת, הגדר `privacy_mode = false` בקובץ `config.toml`
        - לביטול מצב שינה של המדפסת:
            1. Discover the printer with `brother_ql discover`, it returns something like `Found compatible printer QL-600 at: usb://0x04f9:0x20c0/000H2G258173` were `usb://0x04f9:0x20c0/000H2G258173` is the printer id
            2. Set the `power-off-delay` to 0: `brother_ql -p <PRINTER ID> configure set power-off-delay 0`. You can check the set value `brother_ql -p <PRINTER ID> configure get power-off-delay`
        - [Repo](https://github.com/5shekel/printit)

        הדפיסו המון זה הכי טוב!
        """
    )
    st.image(Image.open("assets/station_sm.jpg"), caption="TAMI printshop", width='stretch')
