
@echo off
pushd %~dp0

where uv.exe >nul 2>nul || (
    echo uv.exe not found on PATH. Install it from https://docs.astral.sh/uv/
    exit /b 1
)

echo Running
uv run helldivers2_stratagem

set output=%ERRORLEVEL%

echo Exiting %output%
exit /b %output%
