class AsyncMXL7Firewall:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkL7FirewallRules(self, networkId: str):
        """
        **List the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-l-7-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX L7 firewall'],
            'operation': 'getNetworkL7FirewallRules',
        }
        resource = f'/networks/{networkId}/l7FirewallRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkL7FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-network-l-7-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the MX L7 firewall rules
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX L7 firewall'],
            'operation': 'updateNetworkL7FirewallRules',
        }
        resource = f'/networks/{networkId}/l7FirewallRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

