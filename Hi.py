analytics = # Read Hello Analytics Tutorial for details.

api_query = service.data().ga().get(
    ids=188278934,
    start_date='2012-01-01',
    end_date='2012-01-15',
    metrics='ga:sessions',
    dimensions='ga:source,ga:keyword',
    sort='-ga:sessions,ga:source',
    filters='ga:medium==organic',
    max_results='25')

    try:
  results = get_api_query(service).execute()
  print_results(results)

except TypeError, error:
  # Handle errors in constructing a query.
  print ('There was an error in constructing your query : %s' % error)

except HttpError, error:
  # Handle API service errors.
  print ('There was an API error : %s : %s' %
         (error.resp.status, error._get_reason()))
