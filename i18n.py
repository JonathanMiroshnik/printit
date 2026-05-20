# -*- coding: utf-8 -*-
"""
Internationalization (i18n) module for Sticker Factory.

Provides translated strings for English and Hebrew.
Language is determined by the `language` setting in config.toml.
Default is "english".
"""

import logging

logger = logging.getLogger("sticker_factory.i18n")


TRANSLATIONS = {
    # ---- printit.py ----
    "secrets_not_found": {
        "english": "secrets.toml file not found!",
        "hebrew": "קובץ secrets.toml לא נמצא!",
    },
    "app_subtitle": {
        "english": ":primary[:printer: Print images and text]",
        "hebrew": ":primary[:printer: הדפסות של תמונות וטקסט]",
    },
    "sidebar_title": {
        "english": ":primary[Settings]",
        "hebrew": ":primary[הגדרות]",
    },
    "select_printer": {
        "english": ":primary[Select Printer]",
        "hebrew": ":primary[בחירת מדפסת]",
    },
    "available_printer": {
        "english": "**Available Printer**",
        "hebrew": "**מדפסת זמינה**",
    },
    "no_printers_found": {
        "english": "No available printers found! Check connections, power and paper.",
        "hebrew": "לא נמצאו מדפסות זמינות! בדוק חיבורים, חשמל ונייר.",
    },
    "printers_detected": {
        "english": "Printers detected",
        "hebrew": "מדפסות שזוהו",
    },
    "label_size": {
        "english": "Label Size",
        "hebrew": "גודל תווית",
    },
    "status": {
        "english": "Status",
        "hebrew": "סטטוס",
    },
    "no_tabs_enabled": {
        "english": "No tabs enabled! Check the enabled tabs configuration in config.toml",
        "hebrew": "שום לשונית לא מופעלת! בדוק את תצורת enabled tabs בקובץ config.toml",
    },
    "tab_not_implemented": {
        "english": "The tab '{}' is not implemented yet",
        "hebrew": "הלשונית '{}' עדיין לא מומשה",
    },
    "tab_error": {
        "english": "Error processing tab {}: {}",
        "hebrew": "שגיאה בעיבוד הלשונית {}: {}",
    },
    # ---- tabs/label.py ----
    "label_tab_title": {
        "english": ":printer: Label",
        "hebrew": ":printer: תווית",
    },
    "enter_text": {
        "english": "Enter text to print",
        "hebrew": "הכנס טקסט להדפסה",
    },
    "write_something": {
        "english": "Write something",
        "hebrew": "כתוב משהו",
    },
    "urls_found": {
        "english": "Found URLs: maybe we will auto-convert them to QR code in the future",
        "hebrew": "נמצאו URLs: אולי נהפוך אותם ל-QR code אוטומטית בעתיד",
    },
    "fonts_unavailable_warning": {
        "english": "Custom fonts not available, using system font: {}",
        "hebrew": "גופנים מותאמים אישית לא זמינים, משתמש בגופן מערכת: {}",
    },
    "no_ttf_otf_warning": {
        "english": "No TrueType or OpenType fonts available, using PIL default font",
        "hebrew": "אין גופני TrueType או OpenType זמינים, משתמש בגופן ברירת מחדל של PIL",
    },
    "no_font_error": {
        "english": "Cannot load any font. Please check font installation on your system.",
        "hebrew": "לא ניתן לטעון שום גופן. נא לבדוק את התקנת הגופנים במערכת.",
    },
    "font_settings": {
        "english": "Font settings",
        "hebrew": "הגדרות גופן",
    },
    "select_alignment": {
        "english": "Select text alignment",
        "hebrew": "בחר יישור טקסט",
    },
    "font_size": {
        "english": "Font size",
        "hebrew": "גודל גופן",
    },
    "font_size_help": {
        "english": "Supports TTF and OTF fonts",
        "hebrew": "תומך בגופני TTF ו-OTF",
    },
    "font_load_error": {
        "english": "Font {} not found, using default font.",
        "hebrew": "הגופן {} לא נמצא, משתמש בגופן ברירת מחדל.",
    },
    "font_load_error_warning": {
        "english": "Error loading font {}: {}",
        "hebrew": "שגיאה בטעינת הגופן {}: {}",
    },
    "font_load_error_fatal": {
        "english": "Error loading font: {}",
        "hebrew": "שגיאה בטעינת גופן: {}",
    },
    "add_qr_code": {
        "english": "Add QR code to sticker",
        "hebrew": "הוסף QRcode לסטיקר",
    },
    "print_sticker_qr": {
        "english": "Print sticker+QR",
        "hebrew": "הדפס סטיקר+קוד",
    },
    "print_qr_only": {
        "english": "Print QR only",
        "hebrew": "הדפס סטיקר",
    },
    "print_text_only": {
        "english": "Print sticker",
        "hebrew": "הדפס סטיקר",
    },
    "sticker_sent": {
        "english": "Sticker sent to printer",
        "hebrew": "הסטיקר נשלח למדפסת",
    },
    # ---- tabs/sticker.py ----
    "sticker_tab_title": {
        "english": ":printer: Sticker",
        "hebrew": ":printer: סטיקר",
    },
    "rotate_90": {
        "english": "Rotate - _90 degrees_",
        "hebrew": "סובב - _90 מעלות_",
    },
    "print_button_text": {
        "english": "Print image",
        "hebrew": "הדפס תמונה",
    },
    "clear_selection": {
        "english": "Clear selection",
        "hebrew": "נקה בחירה",
    },
    "image_url_input": {
        "english": "Or enter HTTPS image URL to download and print",
        "hebrew": "או הכנס כתובת HTTPS של תמונה להורדה ולהדפסה",
    },
    "image_loaded_from_history": {
        "english": "Image loaded from history: {}",
        "hebrew": "תמונה נטענה מההיסטוריה: {}",
    },
    # ---- tabs/sticker_pro.py ----
    "sticker_pro_tab_title": {
        "english": ":printer: Sticker Pro",
        "hebrew": ":printer: סטיקר למתקדמים",
    },
    "sticker_pro_url": {
        "english": "Or enter HTTPS image URL to download and process",
        "hebrew": "או הכנס כתובת HTTPS של תמונה להורדה ולעיבוד",
    },
    "pdf_detected": {
        "english": "PDF detected. Converting first page to image.",
        "hebrew": "זוהה קובץ PDF. ממיר את העמוד הראשון לתמונה.",
    },
    "select_dpi": {
        "english": "Select DPI for conversion",
        "hebrew": "בחר DPI להמרה",
    },
    "pymupdf_not_installed": {
        "english": "PyMuPDF (fitz) not installed. Install with: pip install pymupdf",
        "hebrew": "PyMuPDF (fitz) לא מותקן. התקן עם: pip install pymupdf",
    },
    "pdf_error": {
        "english": "Error converting PDF: {}",
        "hebrew": "שגיאה בהמרת PDF: {}",
    },
    "try_image": {
        "english": "Try an image or another format",
        "hebrew": "נסה תמונה או פורמט אחר",
    },
    "choose_print_image": {
        "english": "Choose which image to print/save:",
        "hebrew": "בחר איזה תמונה להדפיס/לשמור:",
    },
    "original_choice": {
        "english": "Original",
        "hebrew": "מקורית",
    },
    "threshold_choice": {
        "english": "Threshold",
        "hebrew": "Threshold",
    },
    "general_options": {
        "english": "General options:",
        "hebrew": "אפשרויות כלליות:",
    },
    "mirror_image": {
        "english": "Mirror image",
        "hebrew": "שיקוף תמונה",
    },
    "invert_colors": {
        "english": "Invert colors",
        "hebrew": "היפוך צבעים",
    },
    "target_width_mm": {
        "english": "Target width (mm)",
        "hebrew": "רוחב מטרה (מ\"מ)",
    },
    "rotate_disabled_note": {
        "english": "Rotation disabled when target width is set",
        "hebrew": "סיבוב מבוטל כשמצוין רוחב מטרה",
    },
    "levels_adjustment": {
        "english": "Levels adjustment:",
        "hebrew": "כיוונון רמות:",
    },
    "black_point": {
        "english": "Black point",
        "hebrew": "נקודה שחורה",
    },
    "white_point": {
        "english": "White point",
        "hebrew": "נקודה לבנה",
    },
    "dither_option": {
        "english": "Dither - Approximate grayscale using dithering",
        "hebrew": "שיטוח (Dither) - קירוב גווני אפור באמצעות שיטוח",
    },
    "threshold_percent": {
        "english": "Threshold (percent)",
        "hebrew": "סף (אחוזים)",
    },
    "meme_top_text": {
        "english": "Top text",
        "hebrew": "טקסט עליון",
    },
    "meme_bottom_text": {
        "english": "Bottom text",
        "hebrew": "טקסט תחתון",
    },
    "meme_font_size": {
        "english": "Meme font size",
        "hebrew": "גודל גופן מים",
    },
    "meme_outline_width": {
        "english": "Meme outline width",
        "hebrew": "עובי קו מתאר מים",
    },
    "print_sent": {
        "english": "Print sent to printer!",
        "hebrew": "ההדפסה נשלחה למדפסת!",
    },
    # ---- tabs/cat.py ----
    "cat_tab_title": {
        "english": ":printer: Cat",
        "hebrew": ":printer: חתול",
    },
    "cat_caption": {
        "english": "Courtesy of https://thecatapi.com/",
        "hebrew": "באדיבות https://thecatapi.com/",
    },
    "fetch_cat": {
        "english": "Fetch cat",
        "hebrew": "שלוף חתול",
    },
    "cat_fetch_error": {
        "english": "Error fetching cat: {}",
        "hebrew": "שגיאה בשליף חתול: {}",
    },
    "cat_caption_image": {
        "english": "Cat!",
        "hebrew": "חתול!",
    },
    "print_cat": {
        "english": "Print cat",
        "hebrew": "הדפס חתול",
    },
    "cat_sent": {
        "english": "Cat sent to printer!",
        "hebrew": "החתול נשלח למדפסת!",
    },
    # ---- tabs/dog.py ----
    "dog_tab_title": {
        "english": ":printer: Dog",
        "hebrew": ":printer: כלבלב",
    },
    "dog_caption": {
        "english": "Courtesy of https://thedogapi.com/",
        "hebrew": "באדיבות https://thedogapi.com/",
    },
    "fetch_dog": {
        "english": "Fetch dog",
        "hebrew": "שלוף כלב",
    },
    "dog_fetch_error": {
        "english": "Error fetching dog: {}",
        "hebrew": "שגיאה בשליף כלב: {}",
    },
    "dog_caption_image": {
        "english": "Dog!",
        "hebrew": "כלב!",
    },
    "print_dog": {
        "english": "Print dog",
        "hebrew": "הדפס כלב",
    },
    "dog_sent": {
        "english": "Dog sent to printer!",
        "hebrew": "הכלב נשלח למדפסת!",
    },
    # ---- tabs/history.py ----
    "history_title": {
        "english": "Label and Sticker Gallery",
        "hebrew": "גלריית תוויות וסטיקרים",
    },
    "search_files": {
        "english": "Search file names",
        "hebrew": "חיפוש שמות קבצים",
    },
    "filter_duplicates": {
        "english": "Filter duplicates",
        "hebrew": "סנן כפילויות",
    },
    "refresh_gallery": {
        "english": "Refresh gallery",
        "hebrew": "רענן גלריה",
    },
    "previous": {
        "english": "Previous",
        "hebrew": "קודם",
    },
    "next": {
        "english": "Next",
        "hebrew": "הבא",
    },
    "print": {
        "english": "Print",
        "hebrew": "הדפס",
    },
    "send_to_sticker": {
        "english": "Send to Sticker",
        "hebrew": "שלח לסטיקר",
    },
    "image_load_error": {
        "english": "Error loading image: {}",
        "hebrew": "שגיאה בטעינת תמונה: {}",
    },
    "no_images_in_history": {
        "english": "No images in history yet. Print some images to see them here!",
        "hebrew": "אין תמונות בהיסטוריה עדיין. הדפס תמונות כדי לראות אותן כאן!",
    },
    # ---- tabs/faq.py ----
    "faq_title": {
        "english": "Frequently Asked Questions:",
    # ---- tabs/webcam.py ----
    "webcam_tab_title": {
        "english": ":printer: A snapshot",
        "hebrew": ":printer: A snapshot",
    },
    "print_rotated": {
        "english": "Print rotated Image",
        "hebrew": "Print rotated Image",
    },
    "image_sent_rotated": {
        "english": "Rotated image sent to printer!",
        "hebrew": "Rotated image sent to printer!",
    },
    "print_webcam": {
        "english": "Print Image",
        "hebrew": "Print Image",
    },
    "image_sent": {
        "english": "Image sent to printer!",
        "hebrew": "Image sent to printer!",
    },
    "ask_camera_permission": {
        "english": "Ask user for camera permission",
        "hebrew": "Ask user for camera permission",
    },
    "take_a_picture": {
        "english": "Take a picture",
        "hebrew": "Take a picture",
    },

    # ---- tabs/text2image.py ----
    "text2image_tab_title": {
        "english": ":printer: Image from text",
        "hebrew": ":printer: Image from text",
    },
    "t2i_subtitle": {
        "english": "Using TAMI Stable Diffusion bot",
        "hebrew": "Using TAMI Stable Diffusion bot",
    },
    "enter_prompt": {
        "english": "Enter a prompt",
        "hebrew": "Enter a prompt",
    },
    "generating_image": {
        "english": "Generating image from prompt: {}",
        "hebrew": "Generating image from prompt: {}",
    },
    "original_image_cap": {
        "english": "Original Image",
        "hebrew": "Original Image",
    },
    "dithered_image_cap": {
        "english": "Resized and Dithered Image",
        "hebrew": "Resized and Dithered Image",
    },
    "print_original": {
        "english": "Print Original Image",
        "hebrew": "Print Original Image",
    },
    "original_sent": {
        "english": "Original image sent to printer!",
        "hebrew": "Original image sent to printer!",
    },
    "print_dithered": {
        "english": "Print Dithered Image",
        "hebrew": "Print Dithered Image",
    },
    "dithered_sent": {
        "english": "Dithered image sent to printer!",
        "hebrew": "Dithered image sent to printer!",
    },

    # ---- tabs/faq.py ----

        "hebrew": "שאלות נפוצות:",
    },
    # ---- printer_utils.py ----
    "print_status": {
        "english": "Print status: {}",
        "hebrew": "סטטוס הדפסה: {}",
    },
    "print_completed": {
        "english": "Print completed successfully!",
        "hebrew": "ההדפסה הושלמה בהצלחה!",
    },
    "sticker_saved_as": {
        "english": "Sticker saved as {}",
        "hebrew": "הסטיקר נשמר בשם {}",
    },
    "print_failed": {
        "english": "Print failed: {}",
        "hebrew": "ההדפסה נכשלה: {}",
    },
}


def _(key, *args):
    """Translate a key to the current language."""
    lang = _get_language()
    entry = TRANSLATIONS.get(key)
    if entry is None:
        logger.warning(f"Missing translation key: {key}")
        return key
    text = entry.get(lang) or entry.get("english", key)
    if args:
        try:
            return text.format(*args)
        except (IndexError, KeyError) as e:
            logger.warning(f"Format error for key {key}: {e}")
            return text
    return text


def _get_language():
    """Determine the active language with caching."""
    global _LANGUAGE_CACHE
    if _LANGUAGE_CACHE is not None:
        return _LANGUAGE_CACHE
    try:
        from config_manager import LANGUAGE
        _LANGUAGE_CACHE = LANGUAGE if LANGUAGE in ("english", "hebrew") else "english"
        logger.info(f"Language set to: {_LANGUAGE_CACHE}")
    except Exception as e:
        logger.warning(f"Could not load language from config, defaulting to english: {e}")
        _LANGUAGE_CACHE = "english"
    return _LANGUAGE_CACHE


_LANGUAGE_CACHE = None


def t(key, *args):
    """Shorthand alias for _()."""
    return _(key, *args)

