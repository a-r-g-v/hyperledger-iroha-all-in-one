cd /app/src/
python make_config.py > config.json
sleep 1000
iroha/build/bin/irohad --config /app/src/config.json --genesis_block /app/src/genesis_block/genesis.block  --keypair_name /app/src/keys/node0
