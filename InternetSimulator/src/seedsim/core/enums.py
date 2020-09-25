from enum import Enum

class NetworkType(Enum):
    """!
    @brief Network types enum.
    """

    ## Public internet exchange network
    InternetExchange = "Internet Exchange Network"

    ## Private links netwroks. OSPF routers and IBGP runs on this type of
    #  networks.
    Local = "Local Network"

    ## Host networks. "Content" (i.e., web server, dns server) runs on this type
    #  of networks.
    Host = "Content Network"

class NodeRole(Enum):
    """!
    @brief Node roles enum.
    """

    ## Host node.
    Host = "Host"

    ## Router node.
    Router = "Router"

    ## Route served node.
    RouteServer = "Route Server"

class InterfaceType(Enum):
    """!
    @brief NIC types enum.
    """

    ## Interface connected to IX.
    InternetExchange = "Internet Exchange Interface"

    ## Interface connected to internal transit network, or from router to a host
    #  network
    Local = "Internal Network Interface"

    ## Interface connected to hosting network.
    Host = "Content network Interface"