# Opora BackEnd Challenge

## Installation

```bash
git clone https://github.com/tomer92808888/Opora-Project.git
cd Opora-Project
pip install -r requirements.txt
```

## Running

```bash
uvicorn app:main
```

## Endpoints

- ```bash
  drivers_by_season/{season}
  ```
  Returns a json file of drivers sorted by the wins in the requested season
- ```bash
  seasons_all_time_ranking/{season}
  ```
  Returns a json file of seasons with the top 3 drivers in each season
- ```bash
  driver_profile/{driver_id_or_name}
  ```
  Returns a specific driver (by id/name) with all of his races sorted by date from newest to the oldest
