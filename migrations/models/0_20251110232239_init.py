from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "book" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL UNIQUE,
    "description" TEXT,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztll1P2zAUhv9KlKtOYgi68qHdhdKNTrSdINsQCEVu7KZWHTskzmiF+t/n4yR1kn6IVb"
    "AOibvmPe+Jz3ns1OfJDgUmLNk/E2Jif7aebI5Con5U9D3LRlFkVBAkGjJtHBaOYSJj5Eul"
    "jRBLiJIwSfyYRpIKrlSeMgai8JWR8sBIKacPKfGkCIgck1gF7u6VTDkmU5IUj9HEG1HCcK"
    "VMimFtrXtyFmmty+UXbYTVhp4vWBpyY45mciz4wk25BDUgnMRIEni9jFMoH6rLuyw6yio1"
    "lqzEUg4mI5QyWWr3mQx8wYGfqibRDQawysfmYeukdfrpuHWqLLqShXIyz9ozvWeJmkDfte"
    "c6jiTKHBqj4SapVK9bQtceo3g1u0VCDZ8quo6vgLVTfiGaeozwQI4B2tHRBlo/nav2hXPV"
    "UK4P0ItQxzg72/081MxigNQgLFe2BNIl0zWHsJa2Fc4c1oJmYTE4zSf4Mjw34HM7Ny7UHC"
    "bJAytTa/ScGw00nOWRy0H/a2EvUW5fDs5qcP2YQPsekstsz1VE0pCs5lvNrOHFeep+8WOb"
    "s/v6tG3VAx5wNsv3ehP9bq9z7Tq975UtOHfcDkSaFfyF2jiunfPFS6xfXffCgkfrdtDvaI"
    "IikUGsVzQ+99aGmlAqhcfFo4dw6Rsu1AJMZWPTCG+5sdXM943d6cbq4uFWHk1K9wsIQ+RP"
    "HlGMvaWIaIp13uVQ2AzrCuIo0LsCbKHKfEZxSEz98arpJY9snF+Q8bxPMG9ogvlN4mTl1b"
    "t+himlvMwU8w/+MF5/joFP4y8g5va3CfDw4OAZAJVrLUAdq80qgkvCV9xn364H/TVDikmp"
    "gfzBVYN3mPpyz2I0kff/J9YNFKHrzfNgffSrXUbwApgHd3q9zP8ABdfQaw=="
)
