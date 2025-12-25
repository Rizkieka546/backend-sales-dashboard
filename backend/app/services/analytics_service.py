from app.utils.data_loader import load_data

class AnalyticsService:
    def __init__(self):
        self.df = load_data()

    def summary(self):
        total_records = len(self.df)
        total_amount = float(self.df["amount"].sum())
        average_amount = float(self.df["amount"].mean())

        daily = self.df.groupby("date")["amount"].sum().sort_index()
        growth = 0.0
        if len(daily) > 1:
            growth = ((daily.iloc[-1] - daily.iloc[0]) / daily.iloc[0]) * 100

        return {
            "total_records": total_records,
            "total_amount": round(total_amount, 2),
            "average_amount": round(average_amount, 2),
            "growth_percentage": round(growth, 2),
        }

    def timeseries(self):
        grouped = self.df.groupby("date")["amount"].sum().reset_index()

        return [
            {
                "date": row["date"].strftime("%Y-%m-%d"),
                "total_amount": float(row["amount"]),
            }
            for _, row in grouped.iterrows()
        ]

    def category(self):
        grouped = (
            self.df.groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values("amount", ascending=False)
        )

        return [
            {
                "category": row["category"],
                "total_amount": float(row["amount"]),
            }
            for _, row in grouped.iterrows()
        ]
