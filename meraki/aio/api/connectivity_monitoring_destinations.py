class AsyncConnectivityMonitoringDestinations:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-connectivity-monitoring-destinations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Connectivity monitoring destinations'],
            'operation': 'getNetworkConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/connectivityMonitoringDestinations'

        return await self._session.get(metadata, resource)

    async def updateNetworkConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-network-connectivity-monitoring-destinations
        
        - networkId (string)
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Connectivity monitoring destinations'],
            'operation': 'updateNetworkConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/connectivityMonitoringDestinations'

        body_params = ['destinations']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

