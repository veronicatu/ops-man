mongoimport --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000 -d campaigns -c donations --file ./data/campaign_part_1000000.json

# Some Load
(sleep 0; echo "Starting 1"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=1' ./generate-profiledata-scenario1.js) &
(sleep 0; echo "Starting 2"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=2' ./generate-profiledata-scenario1.js) &
(sleep 0; echo "Starting 3"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=3' ./generate-profiledata-scenario1.js) &
(sleep 0; echo "Starting 4"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=4' ./generate-profiledata-scenario1.js) &
(sleep 0; echo "Starting 5"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=5' ./generate-profiledata-scenario1.js) &
(sleep 0; echo "Starting 6"; mongo --host rsVenus/ip-172-31-1-187:27000,ip-172-31-11-154:27000,ip-172-31-3-117:27000  --quiet --eval 'var col=6' ./generate-profiledata-scenario1.js) &
