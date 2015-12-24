@echo off
setlocal
set /p msg="Enter Commit Message: "
git add *
git commit -m %msg%
git push
endlocal