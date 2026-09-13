from pathlib import Path

from analysis import (
    calculate_statistics,
    create_bar_chart,
    filter_data,
    load_data,
)


BASE_DIRECTORY = Path(__file__).resolve().parent
DATA_FILE = BASE_DIRECTORY / "data" / "inference_data.csv"
OUTPUT_DIRECTORY = BASE_DIRECTORY / "output"


def get_threshold():
    """Menerima dan mengesahkan nilai ambang daripada pengguna."""
    while True:
        try:
            threshold = float(
                input(
                    "Masukkan nilai confidence threshold "
                    "antara 0 hingga 1: "
                )
            )

            if 0 <= threshold <= 1:
                return threshold

            print(
                "Ralat: Nilai confidence mesti antara 0 hingga 1."
            )

        except ValueError:
            print("Ralat: Sila masukkan nombor yang sah.")


def display_results(statistics, threshold):
    """Memaparkan keputusan analisis dengan tersusun."""
    print("\n======================================")
    print("ANALISIS DATA INFERENS AI")
    print("======================================")
    print(f"Confidence threshold       : {threshold:.2f}")
    print(
        f"Jumlah keseluruhan rekod   : "
        f"{statistics['total_records']}"
    )
    print(
        f"Jumlah pengesanan diterima : "
        f"{statistics['accepted_records']}"
    )
    print(
        f"Purata confidence          : "
        f"{statistics['average_confidence']:.2f}"
    )
    print(
        f"Confidence tertinggi       : "
        f"{statistics['highest_confidence']:.2f}"
    )
    print(
        f"Confidence terendah        : "
        f"{statistics['lowest_confidence']:.2f}"
    )
    print(
        f"Purata masa inferens       : "
        f"{statistics['average_inference_time']:.2f} ms"
    )

    print("======================================")
    print("JUMLAH OBJEK")
    print("======================================")

    if statistics["object_counts"]:
        for object_class, total in statistics[
            "object_counts"
        ].items():
            print(f"{object_class:<20}: {total}")
    else:
        print("Tiada objek melepasi nilai ambang.")


def main():
    """Mengawal perjalanan utama program."""
    try:
        data = load_data(DATA_FILE)

        print("\nLIMA REKOD PERTAMA")
        print("==================")
        print(data.head().to_string(index=False))

        threshold = get_threshold()
        filtered_data = filter_data(data, threshold)

        statistics = calculate_statistics(
            filtered_data,
            len(data),
        )

        display_results(statistics, threshold)

        OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

        filtered_file = OUTPUT_DIRECTORY / "filtered_data.csv"
        chart_file = OUTPUT_DIRECTORY / "object_count.png"

        filtered_data.to_csv(filtered_file, index=False)
        chart_created = create_bar_chart(
            filtered_data,
            chart_file,
        )

        print("\n======================================")
        print(f"Data ditapis disimpan: {filtered_file}")

        if chart_created:
            print(f"Graf disimpan: {chart_file}")

    except FileNotFoundError as error:
        print(f"Ralat: {error}")

    except (ValueError, KeyError) as error:
        print(f"Ralat data: {error}")

    except Exception as error:
        print(f"Ralat tidak dijangka: {error}")


if __name__ == "__main__":
    main()