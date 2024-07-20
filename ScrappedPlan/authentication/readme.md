# RTE France Authentication API

This guide explains how to integrate RTE France's Authentication API. The API allows you to obtain a bearer token to authenticate requests for accessing various RTE France services.

## Requirements

- Access credentials (token) for RTE France API. Obtain these from RTE France's developer portal.
- An application created for Generation Forecast with a Client ID and Client Secret.

## Setup

### Obtain API Access Token

1. Sign in to RTE France's developer portal.
2. Navigate to the "My Applications" section to obtain the Client ID and Client Secret.
3. Use these credentials to generate a Base64-encoded API access token, which will be used to authenticate requests and obtain the bearer token.

### Example Response

Upon successful authentication, you will receive a response similar to the following:

```json
{
    "access_token": "...",
    "token_type": "Bearer",
    "expires_in": 7200
}
```

## References

1. [RTE Authentication Documentation](https://data.rte-france.org/documents/20182/22648/EN_GuideOauth2_v5.1.pdf/54d3d183-f20f-4290-9417-bcae122b9e46)
2. [RTE Authentication Apps](https://data.rte-france.com/group/guest/apps)