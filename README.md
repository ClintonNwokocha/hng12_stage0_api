# hng12_stage0_api
A simple Django-based public API that returns my email, current datetime and GitHub repo link

## Description
This is a simple Django API that returns:
- Your registered email address.
- The current datetime.
- The GitHUb URL of the project.

# API Endpoint
- **URL**: [https://hng12-stage0-api-1yuv.onrender.com/api/info/](https://hng12-stage0-api-1yuv.onrender.com/api/info/)
- **Method**: 'GET'
- **Response**:
```json
  {
  "email": "leoclinton2011@hotmail.com",
  "current_datetime": "2025-01-29T18:38:04.524859+00:00",
  "github_url": "https://github.com/ClintonNwokocha/hng12_stage0_api"
  }
