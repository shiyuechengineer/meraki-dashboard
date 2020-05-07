class AsyncMXPortForwardingRules:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkPortForwardingRules(self, networkId: str):
        """
        **Return the port forwarding rules for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-port-forwarding-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'getNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkPortForwardingRules(self, networkId: str, rules: list):
        """
        **Update the port forwarding rules for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-network-port-forwarding-rules
        
        - networkId (string)
        - rules (array): An array of port forwarding params
        """

        kwargs = locals()

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'updateNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

