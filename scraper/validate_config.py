import datetime
def validate_config(config):
  # check if all required fields are present
  required_fields = ['coordinates', 'search_term', 'clean', 'twitterExtract', 'limit', 'scrape_type', ]
  for field in required_fields:
    if field not in config:
      return f"Missing required field: {field}"

  # check if coordinates are correct
  coordinates = config['coordinates']
  if 'long' not in coordinates or 'lat' not in coordinates or 'radius' not in coordinates:
    return "Invalid coordinates"
  try:
    long = float(coordinates['long'])
    lat = float(coordinates['lat'])
    radius = float(coordinates['radius'])
  except ValueError:
    return "Coordinates must be floats"
  if long < -180 or long > 180 or lat < -90 or lat > 90 or radius <= 0:
    return "Invalid coordinates"

  # check if search_term is a non-empty string
  search_term = config['search_term']
  if not isinstance(search_term, str) or not search_term:
    return "Search term must be a non-empty string"


  # check if clean, twitterExtract, and weekly are boolean
  for field in ['clean', 'twitterExtract', 'analysis']:
    value = config[field]
    if value not in ['true', 'false']:
      return f"{field} must be 'true' or 'false'"

  # If scrape_type is custom, check if start_date and end_date are present
  # and in the correct format
  scrape_type = config['scrape_type']
  if scrape_type == 'custom':
    if 'start_date' not in config or 'end_date' not in config:
      return "Missing required field(s) for custom scrape"
    for field in ['start_date', 'end_date']:
      try:
        datetime.datetime.strptime(config[field], '%Y-%m-%d')
      except ValueError:
        return f"Invalid date format for {field}"

  # check if limit is an integer
  try:
    limit = int(config['limit'])
  except ValueError:
    return "Limit must be an integer"

  # check if year and week are integers
  for field in ['year', 'week']:
    try:
      int(config[field])
    except ValueError:
      return f"{field} must be an integer"

  # config is valid
  return True