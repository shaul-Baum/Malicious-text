# שלב 1: תמונת בסיס של פייתון
FROM python:3.11-slim

# שלב 2: הגדרת תיקיית העבודה
WORKDIR /app

# שלב 3: העתקת קבצי הדרישות
COPY requirements.txt .

# שלב 4: התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# שלב 5: העתקת שאר קבצי האפליקציה
COPY . .

# שלב 6: פתיחת פורט 8000
EXPOSE 8000

# שלב 7: הפעלת האפליקציה עם uvicorn
CMD ["uvicorn", "api:main", "--host", "0.0.0.0", "--port", "8000"]
