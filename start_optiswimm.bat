@echo off

start powershell -NoExit -Command "cd C:\Users\Utilisateur\Desktop\OPTISWIMM\backend; .\venv\Scripts\activate; uvicorn app.main:app --reload"

start powershell -NoExit -Command "cd 'C:\Program Files\PostgreSQL\16\bin'; .\psql.exe -U postgres -d optiswimm_db"