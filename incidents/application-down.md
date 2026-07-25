# Incident Report: Application Down

## Incident Summary

**Incident Name:** Flask Application Unavailable  
**Severity:** Critical  
**Status:** Resolved  

## Description

The Flask application became unavailable and stopped responding to health checks. The issue was detected automatically by Prometheus monitoring.

## Impact

- Application requests failed during the outage period.
- Users could not access the application.
- Monitoring alerts were triggered.

## Detection

The Prometheus alert:

`ApplicationDown`

was triggered when:
