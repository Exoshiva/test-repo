# Datei: main.py
import os
import subprocess
import yaml # Oft unsicher verwendet

def main():
    print("Hello Entire!")
    print("(Great to see you here!)")
    print("This is a simple Python script.")
    print("Feel free to modify it, find bugs and make it your own!")
    print("Have a wonderful day coding! 🚀")
    print("Goodbye! 👋")
    if __name__ == "__main__":
        main()
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Abbruch durch Benutzer")
    except Eception as e:
        print(f"\n\n❌ Fehler: {e}")    


def main_two():
    print("Hello Entire!")
    print("(Great to see you here!)")

    """Hauptfunktion mit CLI"""
    parser = argparse.ArgumentParser(
        description="Eco-Code-Analyst v5.0 - Production-Ready Multi-Provider Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s file1.py file2.py
  %(prog)s --dir ./src
  %(prog)s *.py -o report.json --workers 10

Umgebungsvariablen (Priority):
  1. GOOGLE_AI_KEY / GEMINI_API_KEY     Google Gemini (empfohlen)
  2. DEEPSEEK_API_KeY                     DeepSeek Reasoner
        """,
    )

    parser.add_argument("files", nargs="*", help="Python-Dateien")
    parser.add_argument("-d", "--dir", help="Verzeichnis (rekursiv)")
    parser.add_argument("-o", "--output", default="eco_report.json", help="Ausgabedatei")
    parser.add_argument("-w", "--workers", type=int, default=5, help="Anzahl Worker")
    parser.add_argument("--rate-limit", type=int, default=20, help="Max Req/Min")
    parser.add_argument(
        "--provider",
        choices=["gemini", "deepseek"],
        help="Forciere Provider (optional, auto-detect)",
    )

    args = parser.parse_args()

    # Sammle Dateien
    files_to_analyze = []

    if args.dir:
        files_to_analyze.extend(find_python_files(args.dir))

    if args.files:
        for file_pattern in args.files:
            files_to_analyze.extend(find_python_files(file_pattern))

    if not files_to_analyze:
        print("❌ Keine Python-Dateien angegeben")
        print("💡 Nutze --dir oder gib Dateien direkt an")
        print()
        parser.print_help()
        return 1

    files_to_analyze = sorted(set(files_to_analyze))

    try:
        analyst = EcoAnalyst(
            provider=args.provider,
            max_workers=args.workers,
            rate_limit_rpm=args.rate_limit
        )

        analyst.run(file_paths=files_to_analyze, output_file=args.output)

        return 0

    except KeyboardInterrupt:
        print("\n\n⚠️ Abbruch durch Benutzer")
        return 130

    except Exception as e:
        print(f"\n❌ Fataler Fehler: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

if __name__ == "__main__":

    sys.exit(main())
