import komand
from komand.exceptions import PluginException
from .schema import AgentsShutdownInput, AgentsShutdownOutput, Input, Output, Component


class AgentsShutdown(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_shutdown',
                description=Component.DESCRIPTION,
                input=AgentsShutdownInput(),
                output=AgentsShutdownOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, None)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        return {
            Output.AFFECTED: self.connection.agents_action("shutdown", agent_filter).get("affected", 0)
        }
