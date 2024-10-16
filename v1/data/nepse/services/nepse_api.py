from nepse import Nepse

nepse = Nepse()
nepse.setTLSVerification(False)


class NepseAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_live_market():
        return nepse.getLiveMarket()

    @staticmethod
    def get_nepse_index():
        return nepse.getNepseIndex()

    @staticmethod
    def get_nepse_sub_indices():
        return nepse.getNepseSubIndices()
