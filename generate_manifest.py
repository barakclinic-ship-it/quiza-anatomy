"""
סקריפט ליצירת manifest.json מתוך תיקיית תמונות.

שימוש:
1. שים את הסקריפט הזה בתוך התיקייה שמכילה את תיקיית "images" עם התמונות שלך.
   מבנה לדוגמה:
     quiza-anatomy/
       generate_manifest.py   <- הסקריפט הזה
       images/
         median_nerve.jpg
         ulnar_nerve_2.jpg
         ...

2. הרץ בטרמינל:
     python3 generate_manifest.py

3. יווצר קובץ manifest.json בתיקייה הראשית (quiza-anatomy/).
   צריך להעלות אותו ל-GitHub יחד עם תיקיית images.

4. שם התשובה שמוצג בחידון נגזר משם הקובץ:
   - מחליף קווים תחתונים/מקפים ברווחים
   - מסיר את הסיומת (.jpg, .png וכו')
   לדוגמה: "median_nerve_2.jpg" -> "median nerve 2"

   אם אתה רוצה לשנות שם תצוגה בלי לשנות את שם הקובץ,
   אפשר לערוך את manifest.json ישירות אחרי היצירה ולשנות את השדה "name".

5. כדי שכל שם קובץ יעבוד טוב בקישור באינטרנט (URL), מומלץ:
   - להשתמש רק באנגלית, מספרים, קווים תחתונים ומקפים בשמות הקבצים
   - להימנע מרווחים ועברית בשם הקובץ עצמו (אפשר לשים את העברית רק
     בתוך manifest.json בשדה "name" אם תרצה תשובה בעברית)
"""

import json
import os
import sys

IMAGES_DIR = "images"
OUTPUT_FILE = "manifest.json"
VALID_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def make_name(filename):
    base = os.path.splitext(filename)[0]
    name = base.replace("_", " ").replace("-", " ")
    return name.strip()


def main():
    if not os.path.isdir(IMAGES_DIR):
        print(f"שגיאה: לא נמצאה תיקייה '{IMAGES_DIR}' באותה תיקייה כמו הסקריפט.")
        sys.exit(1)

    files = sorted(
        f for f in os.listdir(IMAGES_DIR)
        if os.path.splitext(f)[1].lower() in VALID_EXT
    )

    if not files:
        print(f"שגיאה: לא נמצאו תמונות בתיקייה '{IMAGES_DIR}'.")
        sys.exit(1)

    images = [{"file": f, "name": make_name(f)} for f in files]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"images": images}, f, ensure_ascii=False, indent=2)

    print(f"נוצר {OUTPUT_FILE} עם {len(images)} תמונות.")
    print("דוגמה לרשומה ראשונה:")
    print(json.dumps(images[0], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
