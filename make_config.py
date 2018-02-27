import json
import os

def make_config():
    pg_opt = "host={postgres_host} port={postgres_port} user={postgres_user} password={postgres_password}".format(
        postgres_host=os.environ.get('IROHA_POSTGRES_HOST', 'localhost'),
        postgres_port=os.environ.get('IROHA_POSTGRES_POST', 5432),
        postgres_user=os.environ.get('IROHA_POSTGRES_USER', 'postgres'),
        postgres_password=os.environ.get('IROHA_POSTGRES_PASSWORD', 'mysecretpassword'))

    data = {
        'block_store_path': os.environ.get('IROHA_BLOCK_STORE_PATH', '/tmp/block_store/'),
        'torii_port': 50051,
        'internal_port': 10001,
        'pg_opt': pg_opt,
        'redis_host': os.environ.get('IROHA_REDIS_HOST', 'localhost'),
        'redis_port': os.environ.get('IROHA_REDIS_PORT', 6379),
        'max_proposal_size': os.environ.get('IROHA_MAX_PROPOSAL_SIZE', 10),
        'proposal_delay': os.environ.get('IROHA_PROPOSAL_DELAY', 5000),
        'vote_delay': os.environ.get('IROHA_VOTE_DELAY', 5000),
        'load_delay': os.environ.get('IROHA_LOAD_DELAY', 5000)
    }

    return data


print(json.dumps(make_config()))
