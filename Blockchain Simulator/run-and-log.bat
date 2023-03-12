@echo off
title mosi-sol blockchain simulator
color 0A

echo _____________________________________________________________________
echo  simulator will be start, then auto-save on (log.json) at the folder
echo  dependencies: "nodejs" - run: "npm install" - (just 1 time)
echo _____________________________________________________________________
echo  when dependencies are ok, then run me!
echo  other way: on node cli "node mosisolSimulator" or "npm run me"
echo _____________________________________________________________________

pause

::log --> txt, dot, md, db, json 
node mosisolSimulator > log.json

color 03
echo finish, look at: log.json
echo mock block scan = block-scan.html
pause