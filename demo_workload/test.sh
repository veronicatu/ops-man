./mongotools-3.0.7/mongo localhost -eval 'var col=1' ./scripts/generate-profiledata-scenario1.js &
./mongotools-3.0.7/mongo localhost -eval 'var col=2' ./scripts/generate-profiledata-scenario1.js &
./mongotools-3.0.7/mongo localhost -eval 'var col=3' ./scripts/generate-profiledata-scenario1.js &
./mongotools-3.0.7/mongo localhost -eval 'var col=4' ./scripts/generate-profiledata-scenario1.js &
./mongotools-3.0.7/mongo localhost -eval 'var col=5' ./scripts/generate-profiledata-scenario1.js &
./mongotools-3.0.7/mongo localhost -eval 'var col=6' ./scripts/generate-profiledata-scenario1.js &
wait
echo Done.
