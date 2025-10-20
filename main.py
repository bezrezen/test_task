import csv
import pytest
from tabulate import tabulate
import argparse


def main():
    get_args()


def get_args():
    parser = argparse.ArgumentParser(
        description="Calculate and display average rating per brand from CSV"
    )

    parser.add_argument(
        "--files", nargs="+", required=True, type=argparse.FileType("r")
    )
    parser.add_argument("--report", nargs="+", required=True)

    args = parser.parse_args()

    if args.report != ["average", "rating"]:
        parser.error(f"Unsupported report type: {' '.join(args.report)}.")

    if args.report == ["average", "rating"]:
        sorted_brands = average_rating_report(args.files)
        draw_table(sorted_brands)


def average_rating_report(files):
    brand_ratings = {}
    brand_counts = {}

    for file in files:
        reader = csv.DictReader(file)
        for row in reader:
            brand = row["brand"]
            rating = float(row["rating"])
            if brand in brand_ratings:
                brand_ratings[brand] += rating
                brand_counts[brand] += 1
            else:
                brand_ratings[brand] = rating
                brand_counts[brand] = 1

    brand_avg_rating = {
        brand: brand_ratings[brand] / brand_counts[brand] for brand in brand_ratings
    }

    sorted_brands = sorted(brand_avg_rating.items(), key=lambda x: x[1], reverse=True)
    return sorted_brands


def draw_table(sorted_brands):
    print(
        tabulate(
            sorted_brands,
            headers=["brand", "rating"],
            tablefmt="psql",
            showindex=range(1, len(sorted_brands) + 1),
        )
    )


if __name__ == "__main__":
    main()
