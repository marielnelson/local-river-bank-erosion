class BankProfile:
    def __init__(self, data, transect_idx, survey_date):
        self.transect_idx = transect_idx
        self.survey_date = survey_date
        self.raw_data = data.copy()
        self.data = data.copy()
        self.metadata = {}
        