@echo off
setlocal
set /p msg="Enter Commit Message: "
echo %msg%
git add *
git commit -m %msg%
git push
endlocal