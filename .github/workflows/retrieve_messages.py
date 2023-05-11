name: Populate Messages

on:
  schedule:
    - cron: "*/1 * * * *"  # Run once pep

jobs:
  populate_messages:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install python-telegram-bot

      - name: Retrieve Telegram Messages
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
        run: |
          python retrieve_messages.py > messages.json
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add messages.json
          git commit -m "Update messages.json"
          git push
