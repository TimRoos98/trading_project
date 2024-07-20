# RTE France Authentication API

This guide explains how to integrate RTE France's Authentication API. The API allows you to obtain a bearer token to authenticate requests for accessing various RTE France services.

## Requirements

- Access credentials (token) for RTE France API. Obtain these from RTE France's developer portal.
- An application created for Generation Forecast with a Client ID and Client Secret.

## Setup

### Obtain Generation Forecast API

1. Use RTE authentication to get the required bearer token
2. We want to use the SOLAR production type

## Forecast types
- **CURRENT**: Represents the current forecast.
- **ID**: Represents an intraday forecast for the current day.
- **D-1**: Represents a day-ahead forecast for tomorrow.
- **D-2**: Represents a day-ahead forecast for the day after tomorrow.
- **D-3**: Represents a day-ahead forecast for three days from today.


### Example
#### Example Request
Upon successful authentication, you will receive a response similar to the following:

### HTTP/1.1

#### Headers

- Host: digital.iservices.rte-france.com
- Authorization: Bearer CNAPbfmg7GjvtqTTlKqPm8ykP6R8YJFfJPnyjqW8p1v2PW2UX6bF8z

#### Body

N/A (GET request typically does not have a body)

---

## Response

```json
[
    {
        "forecasts": [
            {
                "start_date": "2024-06-01T00:00:00+02:00",
                "end_date": "2024-06-03T00:00:00+02:00",
                "type": "D-1",
                "production_type": "SOLAR",
                "values": [
                    {
                        "start_date": "2024-06-02T00:00:00+02:00",
                        "end_date": "2024-06-02T01:00:00+02:00",
                        "updated_date": "2024-06-01T16:35:00+02:00",
                        "value": 0
                    },
                    {
                        "start_date": "2024-06-02T01:00:00+02:00",
                        "end_date": "2024-06-02T02:00:00+02:00",
                        "updated_date": "2024-06-01T16:35:00+02:00",
                        "value": 0
                    },
                    // Additional entries omitted for brevity
                ]
            }
        ]
    }
]
```

#### Example Response

## References

1. [RTE Generation Forecast API Documentation](https://data.rte-france.com/documents/20182/224298/EN_GU_API_Generation_Forecast_v02.01.00.pdf)
2. [RTE Generation Forecast APP](https://data.rte-france.com/catalog/-/api/generation/Generation-Forecast/v2.1)