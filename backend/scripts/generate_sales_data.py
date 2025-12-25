import random
import csv
from datetime import date, timedelta

CATEGORIES = [
    "Food",
    "Beverage",
    "Electronics",
    "Clothing",
    "Sports",
    "Books",
    "Home & Garden",
]

START_DATE = date(2023, 1, 1)
DAYS = 365  # 1 tahun data

OUTPUT_PATH = "app/data/sales_data.csv"

def generate():
    rows = []
    current_date = START_DATE

    for _ in range(DAYS):
        daily_transactions = random.randint(3, 10)

        for _ in range(daily_transactions):
            rows.append([
                current_date.isoformat(),
                random.choice(CATEGORIES),
                random.randint(20, 500)
            ])

        current_date += timedelta(days=1)

    return rows

def main():
    rows = generate()

    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount"])
        writer.writerows(rows)

    print(f"Generated {len(rows)} records → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
