name: Build Android APK
on: [push]
jobs:
  build-android:
    runs-on: ubuntu-latest  # Burası Windows kalmış olabilir, Ubuntu olması şart!
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'
      - name: Install Buildozer
        run: |
          sudo apt update
          sudo apt install -y git zip unzip autoconf autogen libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip install --user --upgrade buildozer cython virtualenv
      - name: Build with Buildozer
        run: |
          yes | buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: casus_asistan_mobil_paket
          path: bin/*.apk
