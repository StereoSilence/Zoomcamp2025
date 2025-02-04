'''count_rows_yellow_2020'''
SELECT SUM(row_count) as total_rows FROM (
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_01`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_02`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_03`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_04`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_05`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_06`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_07`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_08`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_09`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_10`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_11`
        UNION ALL
        SELECT COUNT(*) as row_count FROM  `kestra-sandbox-13.zoomcamp.yellow_tripdata_2020_12`
)