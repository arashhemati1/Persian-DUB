#!/bin/bash
pg_dump dubbing_db > /backups/dubbing_db_$(date +%F).sql
mongodump --out /data/backup/
