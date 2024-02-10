#!/usr/bin/env bash
# Reset and feed our datbases

# RESET
cat ~/HAYAT/db/reset_dbs.sql | sudo mysql

# FEED
cat ~/HAYAT/db/hayat_dump.sql | sudo mysql hayat_prod_db
cat ~/HAYAT/db/hayat_dump.sql | sudo mysql hayat_dev_db
cat ~/HAYAT/db/hayat_dump.sql | sudo mysql hayat_test_db
