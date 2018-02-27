python make_config.py > /app/src/config.json
iroha --config /app/src/config.json --genesis_block /app/src/genesious_block/genesious.block  --keypair_name /app/src/keys/node
