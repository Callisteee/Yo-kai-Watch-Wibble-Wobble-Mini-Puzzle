@echo off
cd /d "%~dp0"
where py >nul 2>nul && py start_game.py || python start_game.py
