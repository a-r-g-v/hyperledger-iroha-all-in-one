cd /app/src/
python make_config.py > config.json
sleep 30
iroha/build/bin/irohad --config /app/src/config.json --genesis_block /app/src/genesious_block/genesious.block  --keypair_name /app/src/keys/node0
