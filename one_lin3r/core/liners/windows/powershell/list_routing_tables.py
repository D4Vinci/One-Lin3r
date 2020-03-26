class info:
    author      = "Karim shoair (D4Vinci)"
    description = "List current routing table"
    function    = "PrivEsc"
    liner       = 'Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex'
