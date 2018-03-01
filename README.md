## Abstract
You can run single node iroha-network easily using docker-compose (with your genesis block).

## Prepare
If you have your original genesis block or keys,  you can replace following files.

- genesis.block
- keys/

Even if you do not give those files, you can run iroha with already given settings.

## Run

```
docker-compose -p _iroha_name_ up -d
```

See also run.sh
