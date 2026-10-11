# Data Dictionary

## Project
An Integrated Distributed Framework for Automated Lifecycle Classification
and Redundancy Mitigation in Large-Scale Repositories

## 1. Purpose

This document describes the columns available in the processed dataset.
It explains their names, observed data types, and intended uses in file
activity analysis and lifecycle classification.

## 2. Dataset Information

- Format: Parquet
- Total records: 100,000
- Observed file-event period: Approximately July 7–10, 2017
- Unique file paths with recorded events: 7,982

## 3. Column Descriptions

| Column | Description | Intended Use |
|---|---|---|
| id | Record identifier | Identify event records |
| isLocalIP | Indicates whether the IP is classified as local | Network context |
| location | Location-related information | Contextual analysis |
| params | Additional event parameters | Investigate event details |
| role | Role associated with the event | User or role analysis |
| time | Original timestamp string | Preserve original event time |
| type | Processed event type | Count and classify events |
| uid | User identifier | Analyse user-associated activity |
| uidType | Type of user identifier | Interpret user information |
| event_time | Parsed event timestamp | Time-based analysis |
| type_raw | Original or raw event type | Compare raw and processed event types |
| file_path | File path associated with the event | Group events by file |
| loc_city | City associated with location data | Geographic analysis |
| loc_countryCode | Country code | Geographic analysis |
| loc_countryName | Country name | Geographic analysis |
| loc_latitude | Latitude coordinate | Geographic analysis |
| loc_longitude | Longitude coordinate | Geographic analysis |
| loc_continent | Continent associated with location | Geographic analysis |

## 4. Derived Features

The following features are calculated during file activity analysis.

| Feature | Description |
|---|---|
| total_events | Number of recorded events for a file |
| first_seen | Earliest recorded event timestamp for a file |
| last_seen | Latest recorded event timestamp for a file |
| event_types | Number of distinct processed event types for a file |
| activity_span_days | Difference between first_seen and last_seen in days |
| access_count | Number of recorded file-access events |
| last_access | Latest recorded file-access timestamp |
| days_since_last_access | Time between last_access and the dataset reference timestamp |
| lifecycle_class | Preliminary category assigned by the lifecycle rules |

## 5. Event Types Observed

The processed dataset contains the following event types:

- file_accessed
- file_written
- file_updated
- version_deleted
- file_created
- file_deleted
- permission_changed

## 6. Data Limitations

1. The observation period covers approximately three days.
2. Access counts represent events observed in the available sample.
3. The dataset does not contain a file-size field.
4. Missing or unavailable access history must not be interpreted as proof
   that a file is obsolete.
5. The meanings and original data types of some fields should be confirmed
   against the dataset documentation before operational use.

## 7. Usage

This data dictionary supports dataset profiling, file activity aggregation,
lifecycle classification, and future benchmarking.