name: Build EXE
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Clean Install
      run: |
        python -m pip install --upgrade pip
        pip install pyinstaller cryptography requests pypiwin32 --no-warn-script-location

    - name: Build EXE
      run: |
        pyinstaller --onefile --noconsole final_gorev.py

    - name: Upload
      uses: actions/upload-artifact@v3
      with:
        name: sızma_aracı
        path: dist/*.exe
