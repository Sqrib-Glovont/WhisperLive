@echo off

REM Check if the virtual environment directory exists
if not exist .venv-whisperlive (
    echo Creating virtual environment...
    python3.9 -m venv .venv-whisperlive

    REM Activate the virtual environment
    echo Activating virtual environment...
    call .\.venv-whisperlive\Scripts\activate

    REM Upgrade pip
    echo Upgrading pip...
    .\.venv-whisperlive\Scripts\pip install --upgrade pip

    REM Install ipykernel
    echo Installing ipykernel...
    .\.venv-whisperlive\Scripts\pip install ipykernel
) else (
    REM Activate the virtual environment
    echo Activating virtual environment...
    call .\.venv-whisperlive\Scripts\activate
)

REM Install PyTorch and Torchaudio
echo Installing PyTorch and Torchaudio...
.\.venv-whisperlive\Scripts\pip install torch==2.2.2+cu121 torchaudio==2.2.2+cu121 --index-url https://download.pytorch.org/whl/cu121

REM Install other requirements
echo Installing requirements from requirements.txt...
.\.venv-whisperlive\Scripts\pip install -r requirements\client.txt

echo Setup complete.
pause



